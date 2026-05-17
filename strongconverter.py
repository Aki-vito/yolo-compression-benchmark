from PIL import Image
import pillow_heif
import os
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed
from multiprocessing import cpu_count

pillow_heif.register_heif_opener()

def convert_single_image(args):
    """Convert a single image to all formats and compressions."""
    png_file, output_path, compressions = args
    
    try:
        img = Image.open(png_file)
        
        if img.mode in ('RGBA', 'LA', 'P'):
            rgb_img = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            rgb_img.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
        else:
            rgb_img = img.convert('RGB')
        
        base_name = png_file.stem
        
        # WEBP conv
        for quality in compressions['webp']:
            out_file = output_path / 'webp' / f'q{quality}' / f'{base_name}.webp'
            img.save(out_file, 'WEBP', quality=quality)
        
        # JPEG conv
        for quality in compressions['jpeg']:
            out_file = output_path / 'jpeg' / f'q{quality}' / f'{base_name}.jpg'
            rgb_img.save(out_file, 'JPEG', quality=quality)
        
        # HEIC conv
        for quality in compressions['heic']:
            out_file = output_path / 'heic' / f'q{quality}' / f'{base_name}.heic'
            rgb_img.save(out_file, 'HEIF', quality=quality)
        
        img.close()
        rgb_img.close()
        
        return f"✓ {png_file.name}"
    
    except Exception as e:
        return f"✗ {png_file.name}: {str(e)}"

def convert_images(input_folder, output_base_folder, num_workers=None):
    """
    Convert PNG images to WEBP, JPEG, and HEIC with different compressions using parallel processing.
    """
    
    compressions = {
        'webp': [90, 75, 50, 30, 15,10,5],     # WEBP: 0-100 scale
        'jpeg': [90, 75, 50, 30, 15,10,5],     # JPEG: 0-100 scale  
        'heic': [90, 75, 50, 30, 15,10,5]      # HEIC: 0-100 scale
    }
    
    input_path = Path(input_folder)
    output_path = Path(output_base_folder)
    
    for fmt in compressions.keys():
        for quality in compressions[fmt]:
            (output_path / fmt / f"q{quality}").mkdir(parents=True, exist_ok=True)
    
    # Get all PNG files (both .png and .PNG)
    png_files = list(input_path.glob("*.png")) + list(input_path.glob("*.PNG"))
    
    if len(png_files) == 0:
        print(f"ERROR: No PNG images found in {input_path.absolute()}")
        print(f"Files in directory: {list(input_path.glob('*'))[:10]}")  # Show first 10 files
        return
    
    print(f"Found {len(png_files)} PNG images")
    
    # Use all CPU cores if not specified
    if num_workers is None:
        num_workers = cpu_count()
    
    print(f"Using {num_workers} parallel workers")
    
    # Prepare arguments for each image
    tasks = [(png_file, output_path, compressions) for png_file in png_files]
    
    # Process images in parallel
    completed = 0
    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        futures = {executor.submit(convert_single_image, task): task for task in tasks}
        
        for future in as_completed(futures):
            result = future.result()
            completed += 1
            print(f"[{completed}/{len(png_files)}] {result}")
    
    print("\nConversion complete!")

if __name__ == "__main__":
    # Set your paths here
    input_folder = "main"  # Your test folder with PNG images
    output_folder = ""
    
    # Optional: specify number of workers (default uses all CPU cores)
    convert_images(input_folder, output_folder, num_workers=20)



