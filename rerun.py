#%%
from ultralytics import YOLO 
from ultralytics.data.utils import visualize_image_annotations

import cv2

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# %%

# This is the main experiment baseline model, trained a y11n on png images. Got (B/M) : 0.64,0.44,0.63,0.38

model = YOLO("yolo11n-seg.pt")
results = model.train(data='/home/aki/graduation_project/datasets/cityscapes_dataset/data.yaml',epochs=150,mosaic=1, close_mosaic=20, imgsz=2048, device='cuda',batch= 4,copy_paste = 0.0,name="11nano_main")



# %%
model = YOLO("yolo11n-seg.pt")
results = model.train(data='/home/aki/graduation_project/datasets/cityscapes_dataset/HEIC15.yaml',epochs=150,mosaic=1, close_mosaic=20, imgsz=2048, device='cuda',batch= 4,copy_paste = 0.0,name="11nano_heic")

# %%
model = YOLO("yolo11n-seg.pt")
results = model.train(data='/home/aki/graduation_project/datasets/cityscapes_dataset/JPEG15.yaml',epochs=150,mosaic=1, close_mosaic=20, imgsz=2048, device='cuda',batch= 4,copy_paste = 0.0,name="11nano_jpeg")

# %%
model = YOLO("yolo11n-seg.pt")
results = model.train(data='/home/aki/graduation_project/datasets/cityscapes_dataset/WEBP15.yaml',epochs=150,mosaic=1, close_mosaic=20, imgsz=2048, device='cuda',batch= 4,copy_paste = 0.0,name="11nano_webp")

# %%
model = YOLO("/home/aki/runs/segment/11nano_main3/weights/best.pt")
val_11n = model.val(data='/home/aki/graduation_project/datasets/cityscapes_dataset/data.yaml', split='test')

# %%  main model val for all images | main val
results_J01 = model.val(data='/home/aki/graduation_project/datasets/cityscapes_dataset/JPEG01.yaml',split='test')
results_J03 = model.val(data='/home/aki/graduation_project/datasets/cityscapes_dataset/JPEG03.yaml',split='test')
results_J06 = model.val(data='/home/aki/graduation_project/datasets/cityscapes_dataset/JPEG06.yaml',split='test')
results_J10 = model.val(data='/home/aki/graduation_project/datasets/cityscapes_dataset/JPEG10.yaml',split='test')
results_J15 = model.val(data='/home/aki/graduation_project/datasets/cityscapes_dataset/JPEG15.yaml',split='test')
results_J20 = model.val(data='/home/aki/graduation_project/datasets/cityscapes_dataset/JPEG20.yaml',split='test')
results_J30 = model.val(data='/home/aki/graduation_project/datasets/cityscapes_dataset/JPEG30.yaml',split='test')

results_W01 = model.val(data='/home/aki/graduation_project/datasets/cityscapes_dataset/WEBP01.yaml',split='test')
results_W03 = model.val(data='/home/aki/graduation_project/datasets/cityscapes_dataset/WEBP03.yaml',split='test')
results_W06 = model.val(data='/home/aki/graduation_project/datasets/cityscapes_dataset/WEBP06.yaml',split='test')
results_W10 = model.val(data='/home/aki/graduation_project/datasets/cityscapes_dataset/WEBP10.yaml',split='test')
results_W15 = model.val(data='/home/aki/graduation_project/datasets/cityscapes_dataset/WEBP15.yaml',split='test')
results_W20 = model.val(data='/home/aki/graduation_project/datasets/cityscapes_dataset/WEBP20.yaml',split='test')
results_W30 = model.val(data='/home/aki/graduation_project/datasets/cityscapes_dataset/WEBP30.yaml',split='test')

results_H01 = model.val(data='/home/aki/graduation_project/datasets/cityscapes_dataset/HEIC01.yaml',split='test')
results_H03 = model.val(data='/home/aki/graduation_project/datasets/cityscapes_dataset/HEIC03.yaml',split='test')
results_H06 = model.val(data='/home/aki/graduation_project/datasets/cityscapes_dataset/HEIC06.yaml',split='test')
results_H10 = model.val(data='/home/aki/graduation_project/datasets/cityscapes_dataset/HEIC10.yaml',split='test')
results_H15 = model.val(data='/home/aki/graduation_project/datasets/cityscapes_dataset/HEIC15.yaml',split='test')
results_H20 = model.val(data='/home/aki/graduation_project/datasets/cityscapes_dataset/HEIC20.yaml',split='test')
results_H30 = model.val(data='/home/aki/graduation_project/datasets/cityscapes_dataset/HEIC30.yaml',split='test')



# %%


Jsizes = [19.866,29.491,38.707,62.874,89.293,143.155,345.702]
Wsizes = [19.046,22.323,25.190,33.587,45.261,63.488,153.6] 
Hsizes = [6.758,8.397,12.083,27.648,94.413,607.437,1024]
Psize = [2306.8672]


Jmaps = [results_J01.seg.map,results_J03.seg.map,results_J06.seg.map,results_J10.seg.map, results_J15.seg.map,results_J20.seg.map,results_J30.seg.map]
Wmaps = [results_W01.seg.map,results_W03.seg.map,results_W06.seg.map,results_W10.seg.map, results_W15.seg.map,results_W20.seg.map,results_W30.seg.map]
Hmaps = [results_H01.seg.map,results_H03.seg.map,results_H06.seg.map,results_H10.seg.map, results_H15.seg.map,results_H20.seg.map,results_H30.seg.map]
Pmaps = [val_11n.seg.map]

Jmaps5 = [results_J01.seg.map50,results_J03.seg.map50,results_J06.seg.map50,results_J10.seg.map50, results_J15.seg.map50,results_J20.seg.map50,results_J30.seg.map50]
Wmaps5 = [results_W01.seg.map50,results_W03.seg.map50,results_W06.seg.map50,results_W10.seg.map50, results_W15.seg.map50,results_W20.seg.map50,results_W30.seg.map50]
Hmaps5 = [results_H01.seg.map50,results_H03.seg.map50,results_H06.seg.map50,results_H10.seg.map50, results_H15.seg.map50,results_H20.seg.map50,results_H30.seg.map50]


# %% BAR graphs for main model 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import dataframe_image as dfi


plt.figure(figsize=(8, 5))
sns.set_theme(style="whitegrid")

ax = sns.barplot(x=[str(s) for s in Wsizes], y=Wmaps, hue=[str(s) for s in Wsizes], palette="Greens_d")

plt.title("WEBP: Mask mAP vs. File Size YOLO11n")
plt.xlabel("Average File Size (KB)")
plt.ylabel("Mask mAP @50~95")
plt.ylim(0, 1.0)
plt.savefig('/home/aki/graduation_project/rerun/graphs/WEBP_BarChartmainmodel.png', bbox_inches='tight', dpi=600)
plt.show()

plt.figure(figsize=(8, 5))
sns.set_theme(style="whitegrid")

ax = sns.barplot(x=[str(s) for s in Jsizes], y=Jmaps, hue=[str(s) for s in Jsizes], palette="Blues_d")

plt.title("JPEG: Mask mAP vs. File Size YOLO11n")
plt.xlabel("Average File Size (KB)")
plt.ylabel("Mask mAP @50~95")
plt.ylim(0, 1.0)
plt.savefig('/home/aki/graduation_project/rerun/graphs/JPEG_BarChartmainmodel.png', bbox_inches='tight', dpi=600)
plt.show()

plt.figure(figsize=(8, 5))
sns.set_theme(style="whitegrid")

ax = sns.barplot(x=[str(s) for s in Hsizes], y=Hmaps, hue=[str(s) for s in Hsizes], palette="Oranges_d")

plt.title("HEIC: Mask mAP vs. File Size YOLO11n")
plt.xlabel("Average File Size (KB)")
plt.ylabel("Mask mAP @50~95")
plt.ylim(0, 1.0)
plt.savefig('/home/aki/graduation_project/rerun/graphs/HEIC_BarChartmainmodel.png', bbox_inches='tight', dpi=600)
plt.show()


# %%

chart_dataframe = pd.DataFrame({
    'Format': ['JPEG']*7  + ['HEIC']*7 + ['WEPB']*7,
    'File Size (KB)': Jsizes + Wsizes + Hsizes,
    'mAP': Jmaps + Wmaps + Hmaps
})

sns.set_theme(style="whitegrid")
sns.lineplot(data=chart_dataframe,x='File Size (KB)', y="mAP", hue="Format",marker="o")
plt.title("mAP Performance by File Size")
plt.savefig('/home/aki/graduation_project/rerun/graphs/JWHchart_mainmodel.png', bbox_inches='tight', dpi=600)
plt.show()


# %%

all_maps = Jmaps + Wmaps + Hmaps + Pmaps
all_sizes = Jsizes + Wsizes + Hsizes + Psize 
formats =   ['WEBP']*len(Wmaps)+ ['HEIC']*len(Hmaps) + ['JPEG']*len(Jmaps) + ['PNG']

df = pd.DataFrame({'Format': formats, 'Size': all_sizes, 'mAP': all_maps})
df = df.sort_values('mAP')

plt.figure(figsize=(12, 6))
sns.set_theme(style="whitegrid")
sns.barplot(data=df, x='Size', y='mAP', hue='Format', dodge=False, order=df['Size'])

plt.xticks(rotation=45)
plt.title("mAP Performance by File Size - Bar Chart (Ordered)")
plt.savefig('/home/aki/graduation_project/rerun/graphs/JWHBars_mainmodel_ordered.png', bbox_inches='tight', dpi=600)

plt.show()

# %% Attempting deltas table

webp_results = [
    (90,results_W30.seg.map, results_W30.box.map,results_W30.seg.map50, Wsizes[6]),  
    (75,results_W20.seg.map, results_W20.box.map,results_W20.seg.map50,  Wsizes[5]),  
    (50,results_W15.seg.map, results_W15.box.map,results_W15.seg.map50, Wsizes[4]),  
    (30,results_W10.seg.map, results_W10.box.map,results_W10.seg.map50, Wsizes[3]),  
    (15,results_W06.seg.map, results_W06.box.map,results_W06.seg.map50,  Wsizes[2]),
    (10,results_W03.seg.map, results_W03.box.map,results_W03.seg.map50,  Wsizes[1]),
    (5,results_W01.seg.map, results_W01.box.map,results_W01.seg.map50,  Wsizes[0]),

]

heic_results = [
    (90,results_H30.seg.map, results_H30.box.map,results_H30.seg.map50,  Hsizes[6]),  
    (75,results_H20.seg.map, results_H20.box.map,results_H20.seg.map50, Hsizes[5]),  
    (50,results_H15.seg.map, results_H15.box.map,results_H15.seg.map50,  Hsizes[4]),  
    (30,results_H10.seg.map, results_H10.box.map,results_H10.seg.map50, Hsizes[3]),  
    (15,results_H06.seg.map, results_H06.box.map,results_H06.seg.map50,  Hsizes[2]),
    (10,results_H03.seg.map, results_H03.box.map,results_H03.seg.map50,  Hsizes[1]),
    (5,results_H01.seg.map, results_H01.box.map,results_H01.seg.map50, Hsizes[0]),

]

jpeg_results = [
    (90,results_J30.seg.map, results_J30.box.map,results_J30.seg.map50, Jsizes[6]),  
    (75,results_J20.seg.map, results_J20.box.map,results_J20.seg.map50, Jsizes[5]),  
    (50,results_J15.seg.map, results_J15.box.map,results_J15.seg.map50, Jsizes[4]),  
    (30,results_J10.seg.map, results_J10.box.map,results_J10.seg.map50,  Jsizes[3]),  
    (15,results_J06.seg.map, results_J06.box.map,results_J06.seg.map50,  Jsizes[2]),
    (10,results_J03.seg.map, results_J03.box.map,results_J03.seg.map50,  Jsizes[1]),
    (5,results_J01.seg.map, results_J01.box.map,results_J01.seg.map50,  Jsizes[0]),
]

png_result = [(100, val_11n.seg.map, val_11n.box.map, val_11n.seg.map50, Psize[0])]



# %%

# %% Individual tables function

def save_table(name, results, filename):
    _, segs, _, _, sizes = zip(*results)
    df = pd.DataFrame({
        'Quality': qualities[::-1],  
        "Average File Size": [round(s, 3) for s in sizes],
        "mAP": [round(m, 3) for m in segs],
    })
    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.axis("off")
    t = ax.table(cellText=df.values, colLabels=df.columns,
                 loc="center", cellLoc="center")
    t.auto_set_font_size(False)
    t.set_fontsize(12)
    t.scale(1.2, 2)
    for j in range(len(df.columns)):
        t[(0, j)].set_facecolor("#2C3E50")
        t[(0, j)].set_text_props(color="white", weight="bold")
    plt.title(f"{name} Table", fontsize=14, weight="bold", pad=15)
    plt.tight_layout()
    plt.savefig(filename, dpi=200, bbox_inches="tight", facecolor="white")
    plt.show()
    plt.close()

# %%  Creation of the Tables

save_table("HEIC", heic_results , "HEIC_table.png")

save_table("JPEG", jpeg_results , "JPEG_table.png")
save_table("WEBP", webp_results , "WEBP_table.png")

# %% Deltas table function

def save_delta(formats, png, filename):
    p_seg, p_50, p_box, p_sz = png
    # 1. Build DataFrames for each format
    dfs = []
    for name, res in formats:
        qs, segs, boxes, seg50s, sizes = zip(*res)
        dfs.append(pd.DataFrame({
            "Format": name,
            "Quality": [f"q{q}" for q in qs],
            "Size Reduction (%)": [round((p_sz - s) / p_sz * 100, 2) for s in sizes],
            "mAP@90 Drop (%)": [round((p_seg - m) / p_seg * 100, 2) for m in segs],
            "Mask mAP@90": [round(m, 3) for m in segs],
            "Mask mAP@50": [round(m, 3) for m in seg50s],
            "Box mAP": [round(b, 3) for b in boxes],
        }))
    df = pd.concat(dfs, ignore_index=True)


    df["Indicator"] = (df["Size Reduction (%)"] - df["mAP@90 Drop (%)"]).round(3)
    png_df = pd.DataFrame([{
        "Format": "PNG", "Quality": "q100", "Size Reduction (%)": 0.0, "mAP@90 Drop (%)": 0.0,
        "Mask mAP@90": round(p_seg, 3), "Mask mAP@50": round(p_50, 3), "Box mAP": round(p_box, 3), "Indicator": 0.0
    }])

    df = pd.concat([png_df, df], ignore_index=True)
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.axis("off")
    t = ax.table(cellText=df.values, colLabels=df.columns, loc="center", cellLoc="center")
    t.auto_set_font_size(False)
    t.set_fontsize(10)
    t.scale(1.2, 1.8)
    # Header (Original Blue)
    for j in range(len(df.columns)):
        t[(0, j)].set_facecolor("#4472C4")
        t[(0, j)].set_text_props(color="white", weight="bold")
    colors = {"PNG": "#E7E6E6", "WEBP": "#FFF2CC", "JPEG": "#FCE4D6", "HEIC": "#D9E2F3"}
    for i, fmt in enumerate(df["Format"]):
        row_color = colors.get(fmt, "white")
        for j in range(len(df.columns)):
            t[(i + 1, j)].set_facecolor(row_color)
    plt.title("Image Format Robustness Analysis", fontsize=16, weight="bold", pad=20)
    plt.tight_layout()
    plt.savefig(filename, dpi=200, bbox_inches="tight", facecolor="white")
    plt.show()
    plt.close()

save_delta(
    [("HEIC", heic_results), ("WEBP", webp_results), ("JPEG", jpeg_results)],
    (Pmaps[0], val_11n.seg.map50, val_11n.box.map , Psize[0] ),
    "delta_table_thesis.png"
)

# %% Summary Table

def save_summary_table(formats, png, filename):
    p_sz = png[3]
    rows = []
    
    # PNG Row
    rows.append(["PNG", round(png[0], 3), "—", "—", 0.0])
    
    for name, res in formats:
        qs, segs, _, _, sizes = zip(*res)
        
        # Helper to find mAP for specific quality
        def get_val(target_q):
            for q, seg in zip(qs, segs):
                if q == target_q:
                    return round(seg, 3)
            return "—"
            
        m90 = get_val(90)
        m50 = get_val(50)
        m5  = get_val(5)
        
        # Avg Size Reduction across all qualities
        reds = [(p_sz - s) / p_sz * 100 for s in sizes]
        avg_red = round(sum(reds) / len(reds), 1)
        
        rows.append([name, m90, m50, m5, avg_red])
        
    df = pd.DataFrame(rows, columns=["Format", "q90 mAP", "q50 mAP", "q5 mAP", "Avg Size Red. (%)"])
    
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.axis("off")
    
    t = ax.table(cellText=df.values, colLabels=df.columns, loc="center", cellLoc="center")
    t.auto_set_font_size(False)
    t.set_fontsize(11)
    t.scale(1.2, 2)
    
    for j in range(len(df.columns)):
        t[(0, j)].set_facecolor("#4472C4")
        t[(0, j)].set_text_props(color="white", weight="bold")
        
    plt.tight_layout()
    plt.savefig(filename, dpi=200, bbox_inches="tight", facecolor="white")
    plt.show()
    plt.close()

# %%

save_summary_table(
    [("HEIC", heic_results), ("WEBP", webp_results), ("JPEG", jpeg_results)],
    (Pmaps[0], val_11n.seg.map50, val_11n.box.map , Psize[0] ),
    "summary_table_thesis.png"
)

# %%
