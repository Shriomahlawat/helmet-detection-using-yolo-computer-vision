
Data: https://universe.roboflow.com/yolo-do-it-yhopz/helmet-detector-9rzmg-bmd6q


!nvidia-smi
     
Sat Oct 19 14:38:22 2024       
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 535.104.05             Driver Version: 535.104.05   CUDA Version: 12.2     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  Tesla T4                       Off | 00000000:00:04.0 Off |                    0 |
| N/A   43C    P8               9W /  70W |      0MiB / 15360MiB |      0%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
                                                                                         
+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|  No running processes found                                                           |
+---------------------------------------------------------------------------------------+
Step 01 # Install the Ultralytics Package


!pip install ultralytics
     
Collecting ultralytics
  Downloading ultralytics-8.3.17-py3-none-any.whl.metadata (34 kB)
Requirement already satisfied: numpy>=1.23.0 in /usr/local/lib/python3.10/dist-packages (from ultralytics) (1.26.4)
Requirement already satisfied: matplotlib>=3.3.0 in /usr/local/lib/python3.10/dist-packages (from ultralytics) (3.7.1)
Requirement already satisfied: opencv-python>=4.6.0 in /usr/local/lib/python3.10/dist-packages (from ultralytics) (4.10.0.84)
Requirement already satisfied: pillow>=7.1.2 in /usr/local/lib/python3.10/dist-packages (from ultralytics) (10.4.0)
Requirement already satisfied: pyyaml>=5.3.1 in /usr/local/lib/python3.10/dist-packages (from ultralytics) (6.0.2)
Requirement already satisfied: requests>=2.23.0 in /usr/local/lib/python3.10/dist-packages (from ultralytics) (2.32.3)
Requirement already satisfied: scipy>=1.4.1 in /usr/local/lib/python3.10/dist-packages (from ultralytics) (1.13.1)
Requirement already satisfied: torch>=1.8.0 in /usr/local/lib/python3.10/dist-packages (from ultralytics) (2.4.1+cu121)
Requirement already satisfied: torchvision>=0.9.0 in /usr/local/lib/python3.10/dist-packages (from ultralytics) (0.19.1+cu121)
Requirement already satisfied: tqdm>=4.64.0 in /usr/local/lib/python3.10/dist-packages (from ultralytics) (4.66.5)
Requirement already satisfied: psutil in /usr/local/lib/python3.10/dist-packages (from ultralytics) (5.9.5)
Requirement already satisfied: py-cpuinfo in /usr/local/lib/python3.10/dist-packages (from ultralytics) (9.0.0)
Requirement already satisfied: pandas>=1.1.4 in /usr/local/lib/python3.10/dist-packages (from ultralytics) (2.2.2)
Requirement already satisfied: seaborn>=0.11.0 in /usr/local/lib/python3.10/dist-packages (from ultralytics) (0.13.2)
Collecting ultralytics-thop>=2.0.0 (from ultralytics)
  Downloading ultralytics_thop-2.0.9-py3-none-any.whl.metadata (9.3 kB)
Requirement already satisfied: contourpy>=1.0.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib>=3.3.0->ultralytics) (1.3.0)
Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.10/dist-packages (from matplotlib>=3.3.0->ultralytics) (0.12.1)
Requirement already satisfied: fonttools>=4.22.0 in /usr/local/lib/python3.10/dist-packages (from matplotlib>=3.3.0->ultralytics) (4.54.1)
Requirement already satisfied: kiwisolver>=1.0.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib>=3.3.0->ultralytics) (1.4.7)
Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.10/dist-packages (from matplotlib>=3.3.0->ultralytics) (24.1)
Requirement already satisfied: pyparsing>=2.3.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib>=3.3.0->ultralytics) (3.2.0)
Requirement already satisfied: python-dateutil>=2.7 in /usr/local/lib/python3.10/dist-packages (from matplotlib>=3.3.0->ultralytics) (2.8.2)
Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.1.4->ultralytics) (2024.2)
Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.1.4->ultralytics) (2024.2)
Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests>=2.23.0->ultralytics) (3.4.0)
Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.23.0->ultralytics) (3.10)
Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.23.0->ultralytics) (2.2.3)
Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.23.0->ultralytics) (2024.8.30)
Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from torch>=1.8.0->ultralytics) (3.16.1)
Requirement already satisfied: typing-extensions>=4.8.0 in /usr/local/lib/python3.10/dist-packages (from torch>=1.8.0->ultralytics) (4.12.2)
Requirement already satisfied: sympy in /usr/local/lib/python3.10/dist-packages (from torch>=1.8.0->ultralytics) (1.13.3)
Requirement already satisfied: networkx in /usr/local/lib/python3.10/dist-packages (from torch>=1.8.0->ultralytics) (3.4.1)
Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages (from torch>=1.8.0->ultralytics) (3.1.4)
Requirement already satisfied: fsspec in /usr/local/lib/python3.10/dist-packages (from torch>=1.8.0->ultralytics) (2024.6.1)
Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.7->matplotlib>=3.3.0->ultralytics) (1.16.0)
Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2->torch>=1.8.0->ultralytics) (3.0.1)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in /usr/local/lib/python3.10/dist-packages (from sympy->torch>=1.8.0->ultralytics) (1.3.0)
Downloading ultralytics-8.3.17-py3-none-any.whl (876 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 876.6/876.6 kB 23.5 MB/s eta 0:00:00
Downloading ultralytics_thop-2.0.9-py3-none-any.whl (26 kB)
Installing collected packages: ultralytics-thop, ultralytics
Successfully installed ultralytics-8.3.17 ultralytics-thop-2.0.9
Step 02 # Import All the Requried Libraries


import ultralytics
ultralytics.checks()
     
Ultralytics 8.3.17 🚀 Python-3.10.12 torch-2.4.1+cu121 CUDA:0 (Tesla T4, 15102MiB)
Setup complete ✅ (2 CPUs, 12.7 GB RAM, 32.3/112.6 GB disk)

from ultralytics import YOLO
from IPython.display import Image
     
Step # 03 Download Dataset from Roboflow


!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="ZkNMlNnyIa2y7w8zGWMS")
project = rf.workspace("yolo-do-it-yhopz").project("helmet-detector-9rzmg-bmd6q")
version = project.version(1)
dataset = version.download("yolov11")


     
Collecting roboflow
  Downloading roboflow-1.1.48-py3-none-any.whl.metadata (9.7 kB)
Requirement already satisfied: certifi in /usr/local/lib/python3.10/dist-packages (from roboflow) (2024.8.30)
Collecting idna==3.7 (from roboflow)
  Downloading idna-3.7-py3-none-any.whl.metadata (9.9 kB)
Requirement already satisfied: cycler in /usr/local/lib/python3.10/dist-packages (from roboflow) (0.12.1)
Requirement already satisfied: kiwisolver>=1.3.1 in /usr/local/lib/python3.10/dist-packages (from roboflow) (1.4.7)
Requirement already satisfied: matplotlib in /usr/local/lib/python3.10/dist-packages (from roboflow) (3.7.1)
Requirement already satisfied: numpy>=1.18.5 in /usr/local/lib/python3.10/dist-packages (from roboflow) (1.26.4)
Requirement already satisfied: opencv-python-headless==4.10.0.84 in /usr/local/lib/python3.10/dist-packages (from roboflow) (4.10.0.84)
Requirement already satisfied: Pillow>=7.1.2 in /usr/local/lib/python3.10/dist-packages (from roboflow) (10.4.0)
Requirement already satisfied: python-dateutil in /usr/local/lib/python3.10/dist-packages (from roboflow) (2.8.2)
Collecting python-dotenv (from roboflow)
  Downloading python_dotenv-1.0.1-py3-none-any.whl.metadata (23 kB)
Requirement already satisfied: requests in /usr/local/lib/python3.10/dist-packages (from roboflow) (2.32.3)
Requirement already satisfied: six in /usr/local/lib/python3.10/dist-packages (from roboflow) (1.16.0)
Requirement already satisfied: urllib3>=1.26.6 in /usr/local/lib/python3.10/dist-packages (from roboflow) (2.2.3)
Requirement already satisfied: tqdm>=4.41.0 in /usr/local/lib/python3.10/dist-packages (from roboflow) (4.66.5)
Requirement already satisfied: PyYAML>=5.3.1 in /usr/local/lib/python3.10/dist-packages (from roboflow) (6.0.2)
Collecting requests-toolbelt (from roboflow)
  Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl.metadata (14 kB)
Collecting filetype (from roboflow)
  Downloading filetype-1.2.0-py2.py3-none-any.whl.metadata (6.5 kB)
Requirement already satisfied: contourpy>=1.0.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib->roboflow) (1.3.0)
Requirement already satisfied: fonttools>=4.22.0 in /usr/local/lib/python3.10/dist-packages (from matplotlib->roboflow) (4.54.1)
Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.10/dist-packages (from matplotlib->roboflow) (24.1)
Requirement already satisfied: pyparsing>=2.3.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib->roboflow) (3.2.0)
Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests->roboflow) (3.4.0)
Downloading roboflow-1.1.48-py3-none-any.whl (80 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 80.3/80.3 kB 4.7 MB/s eta 0:00:00
Downloading idna-3.7-py3-none-any.whl (66 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 66.8/66.8 kB 7.0 MB/s eta 0:00:00
Downloading filetype-1.2.0-py2.py3-none-any.whl (19 kB)
Downloading python_dotenv-1.0.1-py3-none-any.whl (19 kB)
Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl (54 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 54.5/54.5 kB 5.0 MB/s eta 0:00:00
Installing collected packages: filetype, python-dotenv, idna, requests-toolbelt, roboflow
  Attempting uninstall: idna
    Found existing installation: idna 3.10
    Uninstalling idna-3.10:
      Successfully uninstalled idna-3.10
Successfully installed filetype-1.2.0 idna-3.7 python-dotenv-1.0.1 requests-toolbelt-1.0.0 roboflow-1.1.48
loading Roboflow workspace...
loading Roboflow project...
Downloading Dataset Version Zip in Helmet-Detector-1 to yolov11:: 100%|██████████| 100833/100833 [00:01<00:00, 52513.26it/s]
Extracting Dataset Version Zip to Helmet-Detector-1 in yolov11:: 100%|██████████| 5696/5696 [00:01<00:00, 4600.12it/s]

dataset.location
     
'/content/Helmet-Detector-1'
Step # 04 Train YOLO11 Model on a Custom Dataset


!yolo task=detect mode=train data={dataset.location}/data.yaml model="yolo11n.pt" epochs=50 imgsz=640
     
Downloading https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11n.pt to 'yolo11n.pt'...
100% 5.35M/5.35M [00:00<00:00, 96.8MB/s]
Ultralytics 8.3.17 🚀 Python-3.10.12 torch-2.4.1+cu121 CUDA:0 (Tesla T4, 15102MiB)
engine/trainer: task=detect, mode=train, model=yolo11n.pt, data=/content/Helmet-Detector-1/data.yaml, epochs=50, time=None, patience=100, batch=16, imgsz=640, save=True, save_period=-1, cache=False, device=None, workers=8, project=None, name=train, exist_ok=False, pretrained=True, optimizer=auto, verbose=True, seed=0, deterministic=True, single_cls=False, rect=False, cos_lr=False, close_mosaic=10, resume=False, amp=True, fraction=1.0, profile=False, freeze=None, multi_scale=False, overlap_mask=True, mask_ratio=4, dropout=0.0, val=True, split=val, save_json=False, save_hybrid=False, conf=None, iou=0.7, max_det=300, half=False, dnn=False, plots=True, source=None, vid_stride=1, stream_buffer=False, visualize=False, augment=False, agnostic_nms=False, classes=None, retina_masks=False, embed=None, show=False, save_frames=False, save_txt=False, save_conf=False, save_crop=False, show_labels=True, show_conf=True, show_boxes=True, line_width=None, format=torchscript, keras=False, optimize=False, int8=False, dynamic=False, simplify=True, opset=None, workspace=4, nms=False, lr0=0.01, lrf=0.01, momentum=0.937, weight_decay=0.0005, warmup_epochs=3.0, warmup_momentum=0.8, warmup_bias_lr=0.1, box=7.5, cls=0.5, dfl=1.5, pose=12.0, kobj=1.0, label_smoothing=0.0, nbs=64, hsv_h=0.015, hsv_s=0.7, hsv_v=0.4, degrees=0.0, translate=0.1, scale=0.5, shear=0.0, perspective=0.0, flipud=0.0, fliplr=0.5, bgr=0.0, mosaic=1.0, mixup=0.0, copy_paste=0.0, copy_paste_mode=flip, auto_augment=randaugment, erasing=0.4, crop_fraction=1.0, cfg=None, tracker=botsort.yaml, save_dir=runs/detect/train
Downloading https://ultralytics.com/assets/Arial.ttf to '/root/.config/Ultralytics/Arial.ttf'...
100% 755k/755k [00:00<00:00, 19.8MB/s]
Overriding model.yaml nc=80 with nc=13

                   from  n    params  module                                       arguments                     
  0                  -1  1       464  ultralytics.nn.modules.conv.Conv             [3, 16, 3, 2]                 
  1                  -1  1      4672  ultralytics.nn.modules.conv.Conv             [16, 32, 3, 2]                
  2                  -1  1      6640  ultralytics.nn.modules.block.C3k2            [32, 64, 1, False, 0.25]      
  3                  -1  1     36992  ultralytics.nn.modules.conv.Conv             [64, 64, 3, 2]                
  4                  -1  1     26080  ultralytics.nn.modules.block.C3k2            [64, 128, 1, False, 0.25]     
  5                  -1  1    147712  ultralytics.nn.modules.conv.Conv             [128, 128, 3, 2]              
  6                  -1  1     87040  ultralytics.nn.modules.block.C3k2            [128, 128, 1, True]           
  7                  -1  1    295424  ultralytics.nn.modules.conv.Conv             [128, 256, 3, 2]              
  8                  -1  1    346112  ultralytics.nn.modules.block.C3k2            [256, 256, 1, True]           
  9                  -1  1    164608  ultralytics.nn.modules.block.SPPF            [256, 256, 5]                 
 10                  -1  1    249728  ultralytics.nn.modules.block.C2PSA           [256, 256, 1]                 
 11                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']          
 12             [-1, 6]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 13                  -1  1    111296  ultralytics.nn.modules.block.C3k2            [384, 128, 1, False]          
 14                  -1  1         0  torch.nn.modules.upsampling.Upsample         [None, 2, 'nearest']          
 15             [-1, 4]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 16                  -1  1     32096  ultralytics.nn.modules.block.C3k2            [256, 64, 1, False]           
 17                  -1  1     36992  ultralytics.nn.modules.conv.Conv             [64, 64, 3, 2]                
 18            [-1, 13]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 19                  -1  1     86720  ultralytics.nn.modules.block.C3k2            [192, 128, 1, False]          
 20                  -1  1    147712  ultralytics.nn.modules.conv.Conv             [128, 128, 3, 2]              
 21            [-1, 10]  1         0  ultralytics.nn.modules.conv.Concat           [1]                           
 22                  -1  1    378880  ultralytics.nn.modules.block.C3k2            [384, 256, 1, True]           
 23        [16, 19, 22]  1    433207  ultralytics.nn.modules.head.Detect           [13, [64, 128, 256]]          
YOLO11n summary: 319 layers, 2,592,375 parameters, 2,592,359 gradients, 6.5 GFLOPs

Transferred 448/499 items from pretrained weights
TensorBoard: Start with 'tensorboard --logdir runs/detect/train', view at http://localhost:6006/
wandb: Using wandb-core as the SDK backend. Please refer to https://wandb.me/wandb-core for more information.
wandb: (1) Create a W&B account
wandb: (2) Use an existing W&B account
wandb: (3) Don't visualize my results
wandb: Enter your choice: 
wandb: Enter your choice: 3
wandb: You chose "Don't visualize my results"
wandb: Tracking run with wandb version 0.18.3
wandb: W&B syncing is set to `offline` in this directory.  
wandb: Run `wandb online` or set WANDB_MODE=online to enable cloud syncing.
Freezing layer 'model.23.dfl.conv.weight'
AMP: running Automatic Mixed Precision (AMP) checks with YOLO11n...
AMP: checks passed ✅
train: Scanning /content/Helmet-Detector-1/train/labels... 1702 images, 30 backgrounds, 0 corrupt: 100% 1702/1702 [00:00<00:00, 1792.54it/s]
train: WARNING ⚠️ /content/Helmet-Detector-1/train/images/Bike-Helmet-Review-VS-Nutshell_mp4-0324_jpg.rf.e4a0571f1222a8bfec600370ce4f30d5.jpg: 22 duplicate labels removed
train: WARNING ⚠️ /content/Helmet-Detector-1/train/images/Get-Your-Fit-Just-Right-With-Our-Helmet-Guide-cycling-helmets_mp4-0070_jpg.rf.3bc654b1d11028f9f00cd7662ec7c880.jpg: 53 duplicate labels removed
train: WARNING ⚠️ /content/Helmet-Detector-1/train/images/Get-Your-Fit-Just-Right-With-Our-Helmet-Guide-cycling-helmets_mp4-0085_jpg.rf.9bd4848ca4141c4875ba11c89795fd30.jpg: 9 duplicate labels removed
train: WARNING ⚠️ /content/Helmet-Detector-1/train/images/Get-Your-Fit-Just-Right-With-Our-Helmet-Guide-cycling-helmets_mp4-0151_jpg.rf.09d91c477a0da1ab0df8ff6c07e116d7.jpg: 1 duplicate labels removed
train: WARNING ⚠️ /content/Helmet-Detector-1/train/images/USAPANG-NUTSHELL-BIKE-HELMETS-ABOUT-NUTSHELL-HELMETS-_mp4-0029_jpg.rf.8ed43c3302f0bddc4e1269d52069c1be.jpg: 1 duplicate labels removed
train: New cache created: /content/Helmet-Detector-1/train/labels.cache
WARNING ⚠️ Box and segment counts should be equal, but got len(segments) = 2409, len(boxes) = 2679. To resolve this only boxes will be used and all segments will be removed. To avoid this please supply either a detect or segment dataset, not a detect-segment mixed dataset.
/usr/local/lib/python3.10/dist-packages/albumentations/__init__.py:13: UserWarning: A new version of Albumentations is available: 1.4.18 (you have 1.4.15). Upgrade using: pip install -U albumentations. To disable automatic update checks, set the environment variable NO_ALBUMENTATIONS_UPDATE to 1.
  check_for_updates()
albumentations: Blur(p=0.01, blur_limit=(3, 7)), MedianBlur(p=0.01, blur_limit=(3, 7)), ToGray(p=0.01, num_output_channels=3, method='weighted_average'), CLAHE(p=0.01, clip_limit=(1, 4.0), tile_grid_size=(8, 8))
val: Scanning /content/Helmet-Detector-1/valid/labels... 572 images, 4 backgrounds, 0 corrupt: 100% 572/572 [00:00<00:00, 719.62it/s]
val: WARNING ⚠️ /content/Helmet-Detector-1/valid/images/Hardhats-Helmets-101_-Classification-and-ANSI-Standard-Breakdown_mp4-0217_jpg.rf.b82db26758ac408068753e0555f8b7c9.jpg: 13 duplicate labels removed
val: New cache created: /content/Helmet-Detector-1/valid/labels.cache
WARNING ⚠️ Box and segment counts should be equal, but got len(segments) = 779, len(boxes) = 886. To resolve this only boxes will be used and all segments will be removed. To avoid this please supply either a detect or segment dataset, not a detect-segment mixed dataset.
Plotting labels to runs/detect/train/labels.jpg... 
optimizer: 'optimizer=auto' found, ignoring 'lr0=0.01' and 'momentum=0.937' and determining best 'optimizer', 'lr0' and 'momentum' automatically... 
optimizer: AdamW(lr=0.000588, momentum=0.9) with parameter groups 81 weight(decay=0.0), 88 weight(decay=0.0005), 87 bias(decay=0.0)
TensorBoard: model graph visualization added ✅
Image sizes 640 train, 640 val
Using 2 dataloader workers
Logging results to runs/detect/train
Starting training for 50 epochs...

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       1/50      2.48G     0.7448      3.223      1.148         15        640: 100% 107/107 [00:36<00:00,  2.95it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:07<00:00,  2.45it/s]
                   all        572        886      0.715       0.47      0.592      0.504

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       2/50      2.39G     0.7146      1.709      1.102         17        640: 100% 107/107 [00:35<00:00,  2.98it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:03<00:00,  5.14it/s]
                   all        572        886      0.771      0.701       0.75      0.637

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       3/50      2.41G     0.6805      1.426      1.085         25        640: 100% 107/107 [00:33<00:00,  3.21it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:03<00:00,  5.21it/s]
                   all        572        886      0.748      0.711      0.772      0.676

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       4/50       2.4G     0.6981      1.314      1.095         23        640: 100% 107/107 [00:33<00:00,  3.17it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:03<00:00,  4.75it/s]
                   all        572        886      0.693      0.737      0.782      0.649

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       5/50      2.41G     0.6654      1.196      1.069         15        640: 100% 107/107 [00:32<00:00,  3.33it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:05<00:00,  3.28it/s]
                   all        572        886      0.851       0.78      0.826      0.728

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       6/50      2.41G     0.6517       1.08      1.057         27        640: 100% 107/107 [00:31<00:00,  3.45it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:05<00:00,  3.49it/s]
                   all        572        886      0.808      0.822      0.832      0.737

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       7/50       2.4G     0.6273      1.029      1.043         22        640: 100% 107/107 [00:33<00:00,  3.23it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:03<00:00,  5.20it/s]
                   all        572        886      0.884      0.798       0.84      0.743

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       8/50      2.43G     0.6159       0.95      1.039         16        640: 100% 107/107 [00:33<00:00,  3.24it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:03<00:00,  5.23it/s]
                   all        572        886      0.754      0.833      0.837      0.745

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
       9/50      2.43G     0.5998     0.8879      1.035         10        640: 100% 107/107 [00:33<00:00,  3.20it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:03<00:00,  5.16it/s]
                   all        572        886      0.885      0.842      0.857      0.762

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      10/50      2.41G     0.5851     0.8422      1.026         16        640: 100% 107/107 [00:33<00:00,  3.23it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:03<00:00,  5.12it/s]
                   all        572        886      0.808      0.868      0.861       0.77

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      11/50       2.4G     0.5787     0.8271      1.022         20        640: 100% 107/107 [00:32<00:00,  3.30it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:04<00:00,  3.84it/s]
                   all        572        886      0.859      0.845      0.862      0.776

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      12/50      2.39G       0.56     0.7681      1.011         18        640: 100% 107/107 [00:31<00:00,  3.35it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:05<00:00,  3.03it/s]
                   all        572        886      0.866      0.868      0.862      0.778

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      13/50      2.41G     0.5513     0.7523      1.009         16        640: 100% 107/107 [00:32<00:00,  3.32it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:04<00:00,  3.81it/s]
                   all        572        886       0.85      0.866      0.865      0.783

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      14/50      2.39G       0.54     0.7282      1.002         13        640: 100% 107/107 [00:33<00:00,  3.23it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:03<00:00,  5.27it/s]
                   all        572        886      0.865      0.852       0.87      0.791

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      15/50       2.4G     0.5403     0.7074      1.001         17        640: 100% 107/107 [00:33<00:00,  3.19it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:03<00:00,  5.32it/s]
                   all        572        886      0.896      0.859      0.874      0.797

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      16/50      2.41G      0.533     0.6948      1.002         13        640: 100% 107/107 [00:33<00:00,  3.22it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:03<00:00,  5.06it/s]
                   all        572        886      0.915      0.866      0.877      0.797

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      17/50       2.4G     0.5394     0.6704     0.9979         25        640: 100% 107/107 [00:33<00:00,  3.18it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:03<00:00,  5.14it/s]
                   all        572        886      0.908      0.868      0.888      0.794

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      18/50      2.41G     0.5105     0.6303     0.9792         21        640: 100% 107/107 [00:33<00:00,  3.22it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:04<00:00,  3.66it/s]
                   all        572        886       0.87      0.845      0.873        0.8

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      19/50      2.41G     0.5249     0.6376     0.9876         34        640: 100% 107/107 [00:31<00:00,  3.41it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:05<00:00,  3.32it/s]
                   all        572        886      0.912      0.857      0.883      0.801

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      20/50      2.39G     0.5191     0.6268     0.9878         19        640: 100% 107/107 [00:33<00:00,  3.22it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:03<00:00,  4.71it/s]
                   all        572        886      0.883      0.878      0.873      0.794

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      21/50      2.41G     0.5124     0.6114     0.9822         20        640: 100% 107/107 [00:33<00:00,  3.23it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:03<00:00,  4.99it/s]
                   all        572        886       0.91      0.872      0.886      0.814

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      22/50       2.4G     0.4918     0.5867     0.9681         27        640: 100% 107/107 [00:33<00:00,  3.19it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:03<00:00,  5.34it/s]
                   all        572        886       0.89      0.876      0.882      0.803

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      23/50      2.41G     0.4836     0.5738     0.9679         19        640: 100% 107/107 [00:34<00:00,  3.14it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:03<00:00,  5.25it/s]
                   all        572        886      0.916      0.874      0.889      0.811

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      24/50      2.41G     0.4911      0.573     0.9793         20        640: 100% 107/107 [00:33<00:00,  3.23it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:04<00:00,  3.77it/s]
                   all        572        886      0.883      0.881      0.889      0.812

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      25/50       2.4G     0.4877      0.558     0.9715         17        640: 100% 107/107 [00:31<00:00,  3.40it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:05<00:00,  3.40it/s]
                   all        572        886      0.919       0.86      0.887      0.799

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      26/50      2.41G     0.4748     0.5596     0.9667         17        640: 100% 107/107 [00:32<00:00,  3.25it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:04<00:00,  4.43it/s]
                   all        572        886      0.899      0.876      0.892      0.819

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      27/50      2.42G     0.4728     0.5605     0.9666         21        640: 100% 107/107 [00:32<00:00,  3.29it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:03<00:00,  5.39it/s]
                   all        572        886      0.865      0.892      0.895      0.818

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      28/50      2.41G     0.4793     0.5309     0.9685         21        640: 100% 107/107 [00:33<00:00,  3.19it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:03<00:00,  5.32it/s]
                   all        572        886      0.898       0.88       0.89       0.81

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      29/50      2.41G     0.4576     0.5192     0.9533         15        640: 100% 107/107 [00:33<00:00,  3.22it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:03<00:00,  5.24it/s]
                   all        572        886      0.899      0.866      0.891      0.814

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      30/50      2.41G     0.4463     0.4999       0.95         20        640: 100% 107/107 [00:33<00:00,  3.21it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:03<00:00,  5.01it/s]
                   all        572        886      0.921       0.88      0.891      0.815

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      31/50       2.4G     0.4509     0.4948     0.9585         23        640: 100% 107/107 [00:32<00:00,  3.28it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:04<00:00,  3.81it/s]
                   all        572        886       0.88       0.89      0.888      0.818

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      32/50      2.41G     0.4567     0.4877     0.9603         20        640: 100% 107/107 [00:31<00:00,  3.43it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:05<00:00,  3.23it/s]
                   all        572        886      0.888       0.89      0.895      0.821

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      33/50      2.41G     0.4464     0.4897      0.953         23        640: 100% 107/107 [00:31<00:00,  3.35it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:04<00:00,  4.04it/s]
                   all        572        886      0.911      0.898      0.903      0.823

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      34/50       2.4G     0.4341     0.4739     0.9412         26        640: 100% 107/107 [00:33<00:00,  3.18it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:03<00:00,  4.95it/s]
                   all        572        886      0.935      0.878      0.901      0.828

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      35/50       2.4G     0.4325     0.4839     0.9458         19        640: 100% 107/107 [00:33<00:00,  3.22it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:03<00:00,  5.24it/s]
                   all        572        886       0.91      0.895      0.905      0.824

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      36/50      2.39G     0.4239     0.4634     0.9357         19        640: 100% 107/107 [00:33<00:00,  3.23it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:03<00:00,  5.25it/s]
                   all        572        886      0.945      0.864      0.901      0.826

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      37/50      2.41G     0.4276     0.4719     0.9404         23        640: 100% 107/107 [00:32<00:00,  3.27it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:03<00:00,  4.54it/s]
                   all        572        886      0.926      0.883      0.898      0.822

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      38/50       2.4G     0.4257     0.4564     0.9395         19        640: 100% 107/107 [00:32<00:00,  3.31it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:04<00:00,  3.67it/s]
                   all        572        886      0.918      0.895      0.901      0.827

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      39/50       2.4G     0.4111     0.4464     0.9293         19        640: 100% 107/107 [00:31<00:00,  3.43it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:06<00:00,  2.93it/s]
                   all        572        886      0.938      0.884      0.902      0.829

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      40/50      2.41G     0.4157      0.442     0.9412         26        640: 100% 107/107 [00:31<00:00,  3.39it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:04<00:00,  4.28it/s]
                   all        572        886      0.918      0.893      0.904      0.829
Closing dataloader mosaic
albumentations: Blur(p=0.01, blur_limit=(3, 7)), MedianBlur(p=0.01, blur_limit=(3, 7)), ToGray(p=0.01, num_output_channels=3, method='weighted_average'), CLAHE(p=0.01, clip_limit=(1, 4.0), tile_grid_size=(8, 8))

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      41/50      2.46G     0.3711     0.4306     0.8923         10        640: 100% 107/107 [00:33<00:00,  3.17it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:03<00:00,  5.04it/s]
                   all        572        886      0.929      0.885      0.899      0.828

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      42/50       2.4G     0.3652     0.4111      0.897         12        640: 100% 107/107 [00:32<00:00,  3.26it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:03<00:00,  5.35it/s]
                   all        572        886      0.911      0.892      0.902      0.828

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      43/50      2.41G      0.359     0.3963     0.8885          6        640: 100% 107/107 [00:31<00:00,  3.36it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:03<00:00,  5.28it/s]
                   all        572        886      0.916      0.886      0.902      0.832

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      44/50      2.39G      0.351     0.3928     0.8836          7        640: 100% 107/107 [00:32<00:00,  3.29it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:03<00:00,  5.34it/s]
                   all        572        886      0.925      0.897      0.907      0.836

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      45/50      2.38G       0.35     0.3826     0.8776          7        640: 100% 107/107 [00:32<00:00,  3.29it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:03<00:00,  5.42it/s]
                   all        572        886      0.938      0.878      0.905      0.833

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      46/50      2.39G     0.3475      0.369     0.8762         11        640: 100% 107/107 [00:32<00:00,  3.24it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:03<00:00,  5.15it/s]
                   all        572        886      0.913      0.899      0.901      0.828

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      47/50      2.38G      0.343     0.3742     0.8761         11        640: 100% 107/107 [00:32<00:00,  3.29it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:03<00:00,  5.45it/s]
                   all        572        886       0.92      0.897      0.903      0.832

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      48/50      2.38G     0.3359     0.3581     0.8775          7        640: 100% 107/107 [00:32<00:00,  3.32it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:03<00:00,  4.92it/s]
                   all        572        886      0.927      0.891      0.905      0.837

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      49/50      2.38G     0.3313     0.3601     0.8733         14        640: 100% 107/107 [00:31<00:00,  3.43it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:04<00:00,  4.32it/s]
                   all        572        886      0.925      0.896      0.906      0.838

      Epoch    GPU_mem   box_loss   cls_loss   dfl_loss  Instances       Size
      50/50      2.39G     0.3261     0.3515     0.8658         11        640: 100% 107/107 [00:31<00:00,  3.43it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:05<00:00,  3.44it/s]
                   all        572        886      0.923      0.897      0.907      0.839

50 epochs completed in 0.526 hours.
Optimizer stripped from runs/detect/train/weights/last.pt, 5.5MB
Optimizer stripped from runs/detect/train/weights/best.pt, 5.5MB

Validating runs/detect/train/weights/best.pt...
Ultralytics 8.3.17 🚀 Python-3.10.12 torch-2.4.1+cu121 CUDA:0 (Tesla T4, 15102MiB)
YOLO11n summary (fused): 238 layers, 2,584,687 parameters, 0 gradients, 6.3 GFLOPs
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 18/18 [00:04<00:00,  3.66it/s]
                   all        572        886      0.923      0.897      0.907      0.839
        Cycling Helmet         68         68      0.985          1      0.995      0.988
             half face         32         32      0.984          1      0.995      0.995
              hard hat         67         86      0.952      0.895        0.9      0.869
                helmet        111        114      0.978      0.965      0.989      0.905
        modular helmet         14         14      0.966          1      0.995      0.984
             motorbike         69         84      0.889      0.488      0.593      0.339
          motorcyclist         30         31      0.945      0.968      0.971      0.903
              nutshell         65        106      0.856      0.896      0.948      0.901
                person        105        133      0.843      0.564      0.606      0.435
                 plate         53         60      0.918          1      0.982       0.84
   quarter face helmet         69        143      0.845      0.993      0.919      0.917
         sports helmet         15         15      0.909          1      0.991      0.991
Speed: 0.1ms preprocess, 1.7ms inference, 0.0ms loss, 1.4ms postprocess per image
Results saved to runs/detect/train
wandb:                                                                                
wandb: 
wandb: Run history:
wandb:                  lr/pg0 ▆███▇▇▇▇▇▇▆▆▆▆▆▅▅▅▅▅▄▄▄▄▄▄▃▃▃▃▃▂▂▂▂▂▂▁▁▁
wandb:                  lr/pg1 ▃▆███▇▇▇▇▇▇▆▆▆▆▆▅▅▅▅▅▄▄▄▄▄▄▃▃▃▃▃▂▂▂▂▂▁▁▁
wandb:                  lr/pg2 ▃▆███▇▇▇▇▇▇▆▆▆▆▅▅▅▅▅▅▄▄▄▄▄▄▃▃▃▃▃▂▂▂▂▂▂▁▁
wandb:        metrics/mAP50(B) ▁▅▅▅▆▇▆▇▇▇▇▇▇█▇▇█▇██████████████████████
wandb:     metrics/mAP50-95(B) ▁▂▁▄▄▅▅▆▆▆▆▇▇▆▇▆▇▇▇▇▇▇▇▇▇▇█▇█▇██████████
wandb:    metrics/precision(B) ▃▃▁▅▄▃▆▆▆▅▇▇▇▆▇▇▆▇▆▇▆▇▇▇▆▇█▇█▇█▇█▇▇█▇▇█▇
wandb:       metrics/recall(B) ▁▅▅▅▆▆▇▇▇▇▇▇▇▇▇▇████▇███▇███████████████
wandb:            model/GFLOPs ▁
wandb:        model/parameters ▁
wandb: model/speed_PyTorch(ms) ▁
wandb:          train/box_loss █▇▇▇▆▆▆▅▅▅▅▅▄▅▄▄▄▄▄▄▃▄▃▃▃▃▃▃▃▃▂▂▂▂▂▁▁▁▁▁
wandb:          train/cls_loss █▄▄▃▃▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:          train/dfl_loss █▇▆▇▆▅▅▅▅▅▄▄▄▄▄▄▄▄▄▄▄▄▄▃▃▃▃▃▃▃▃▃▃▂▂▁▁▁▁▁
wandb:            val/box_loss █▇▆▇▆▅▆▅▄▄▃▃▃▃▃▃▃▃▂▂▂▂▂▂▂▂▂▂▂▁▂▁▂▁▁▁▁▁▁▁
wandb:            val/cls_loss █▄▄▄▃▂▃▂▂▂▂▂▂▂▂▂▂▁▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
wandb:            val/dfl_loss █▇▆█▆▄▅▄▄▄▃▂▃▃▂▂▃▂▂▂▂▂▂▂▂▂▂▂▂▂▁▁▁▁▁▁▁▁▁▁
wandb: 
wandb: Run summary:
wandb:                  lr/pg0 2e-05
wandb:                  lr/pg1 2e-05
wandb:                  lr/pg2 2e-05
wandb:        metrics/mAP50(B) 0.90698
wandb:     metrics/mAP50-95(B) 0.83895
wandb:    metrics/precision(B) 0.92259
wandb:       metrics/recall(B) 0.89741
wandb:            model/GFLOPs 6.454
wandb:        model/parameters 2592375
wandb: model/speed_PyTorch(ms) 3.225
wandb:          train/box_loss 0.32607
wandb:          train/cls_loss 0.35151
wandb:          train/dfl_loss 0.8658
wandb:            val/box_loss 0.39097
wandb:            val/cls_loss 0.38
wandb:            val/dfl_loss 0.9125
wandb: 
wandb: You can sync this run to the cloud by running:
wandb: wandb sync /content/wandb/offline-run-20241019_144415-wklplmof
wandb: Find logs at: ./wandb/offline-run-20241019_144415-wklplmof/logs
💡 Learn more at https://docs.ultralytics.com/modes/train
Step # 05 Examine Training Results


Image("/content/runs/detect/train/confusion_matrix.png", width=600)
     


Image("/content/runs/detect/train/labels.jpg", width=600)
     


Image("/content/runs/detect/train/results.png", width=600)
     


Image("/content/runs/detect/train/train_batch0.jpg", width=600)
     


Image("/content/runs/detect/train/val_batch0_pred.jpg", width=600)
     


Image("/content/runs/detect/train/val_batch1_pred.jpg", width=600)
     

Step # 08 Inference with Custom Model on Images


!yolo task=detect mode=predict model="/content/runs/detect/train/weights/best.pt" conf=0.25 source={dataset.location}/test/images save=True
     
Ultralytics 8.3.17 🚀 Python-3.10.12 torch-2.4.1+cu121 CUDA:0 (Tesla T4, 15102MiB)
YOLO11n summary (fused): 238 layers, 2,584,687 parameters, 0 gradients, 6.3 GFLOPs

image 1/568 /content/Helmet-Detector-1/test/images/100-Trajecta-MTB-full-face-helmet-_mp4-0178_jpg.rf.40daedd08d8ee073d606a4e59773f75d.jpg: 640x384 1 sports helmet, 46.2ms
image 2/568 /content/Helmet-Detector-1/test/images/100-Trajecta-MTB-full-face-helmet-_mp4-0179_jpg.rf.53fbc18ec2d3dbc33fa2ca90fe4d27f6.jpg: 640x384 1 sports helmet, 12.5ms
image 3/568 /content/Helmet-Detector-1/test/images/100-Trajecta-MTB-full-face-helmet-_mp4-0186_jpg.rf.4b0cfc853a5cddb12cc069cd568ee13f.jpg: 640x384 1 sports helmet, 13.6ms
image 4/568 /content/Helmet-Detector-1/test/images/100-Trajecta-MTB-full-face-helmet-_mp4-0199_jpg.rf.ab2c103b611fa0377e8d8833d0d99e72.jpg: 640x384 1 sports helmet, 10.4ms
image 5/568 /content/Helmet-Detector-1/test/images/100-Trajecta-MTB-full-face-helmet-_mp4-0202_jpg.rf.ff6838cf4838f7bbf9cd1d75488bceaf.jpg: 640x384 1 sports helmet, 10.1ms
image 6/568 /content/Helmet-Detector-1/test/images/416536556_7209359705787581_7005850060369918163_n_mp4-29_jpg.rf.69938cc37711d04694322384e6ff542d.jpg: 640x384 1 helmet, 11.8ms
image 7/568 /content/Helmet-Detector-1/test/images/416536556_7209359705787581_7005850060369918163_n_mp4-3_jpg.rf.dce763ce7147394af40a9d363f3a601f.jpg: 640x384 1 helmet, 13.7ms
image 8/568 /content/Helmet-Detector-1/test/images/416536556_7209359705787581_7005850060369918163_n_mp4-6_jpg.rf.1990479c2c853027338fd8019dacbb12.jpg: 640x384 1 helmet, 10.7ms
image 9/568 /content/Helmet-Detector-1/test/images/416536556_7209359705787581_7005850060369918163_n_mp4-7_jpg.rf.40ab8e02742463cfeef58b2da1672b9c.jpg: 640x384 1 helmet, 10.4ms
image 10/568 /content/Helmet-Detector-1/test/images/417187305_6952594141526152_5780383563774292459_n_mp4-0_jpg.rf.3dd755fb88bbe0d754be5e83e93e4c96.jpg: 640x384 1 nutshell, 13.6ms
image 11/568 /content/Helmet-Detector-1/test/images/417187305_6952594141526152_5780383563774292459_n_mp4-13_jpg.rf.a3a5bd24394c7ca6a10ec4b9d1ad5b3d.jpg: 640x384 1 nutshell, 13.8ms
image 12/568 /content/Helmet-Detector-1/test/images/417187305_6952594141526152_5780383563774292459_n_mp4-22_jpg.rf.8c8579e50321709e6e46686ca543bfbd.jpg: 640x384 1 nutshell, 10.1ms
image 13/568 /content/Helmet-Detector-1/test/images/417187305_6952594141526152_5780383563774292459_n_mp4-4_jpg.rf.3ed933805ff1d8357fe3a90fdd3c2253.jpg: 640x384 1 nutshell, 10.3ms
image 14/568 /content/Helmet-Detector-1/test/images/417187305_6952594141526152_5780383563774292459_n_mp4-6_jpg.rf.d4a8d672118def27ae10cfe114fa90b5.jpg: 640x384 1 nutshell, 10.8ms
image 15/568 /content/Helmet-Detector-1/test/images/417187305_6952594141526152_5780383563774292459_n_mp4-7_jpg.rf.32f50dda228940d00ce7a65da670ab88.jpg: 640x384 1 nutshell, 12.9ms
image 16/568 /content/Helmet-Detector-1/test/images/417203812_1414466772613301_5116553846369368985_n_mp4-17_jpg.rf.b700b6ca6d89cb62e58697f3cc45de7c.jpg: 640x384 1 helmet, 10.5ms
image 17/568 /content/Helmet-Detector-1/test/images/417203812_1414466772613301_5116553846369368985_n_mp4-19_jpg.rf.02612f77bd5ea9f064a61af5bbe86a5e.jpg: 640x384 1 helmet, 10.5ms
image 18/568 /content/Helmet-Detector-1/test/images/417203812_1414466772613301_5116553846369368985_n_mp4-33_jpg.rf.493e23887e14e4d5dec3dd28c9556174.jpg: 640x384 1 helmet, 10.7ms
image 19/568 /content/Helmet-Detector-1/test/images/417203812_1414466772613301_5116553846369368985_n_mp4-4_jpg.rf.2cd509613694197446af39899b2aec03.jpg: 640x384 1 helmet, 10.5ms
image 20/568 /content/Helmet-Detector-1/test/images/418471435_24447969008180394_5472362831271600481_n_mp4-10_jpg.rf.9076c8ba17bb09dedde40626ded1e566.jpg: 640x480 1 nutshell, 74.1ms
image 21/568 /content/Helmet-Detector-1/test/images/418471435_24447969008180394_5472362831271600481_n_mp4-15_jpg.rf.9eab6f6f5e1ef4e9a400dafcd350d549.jpg: 640x480 1 nutshell, 10.6ms
image 22/568 /content/Helmet-Detector-1/test/images/418471435_24447969008180394_5472362831271600481_n_mp4-22_jpg.rf.3fba957a476bdde88eaab39bc8381199.jpg: 640x480 1 nutshell, 10.5ms
image 23/568 /content/Helmet-Detector-1/test/images/Bike-Helmet-Review-VS-Nutshell_mp4-0360_jpg.rf.014194d6d07710a4c29b4835d5c30570.jpg: 384x640 1 nutshell, 63.8ms
image 24/568 /content/Helmet-Detector-1/test/images/Bike-Helmet-Review-VS-Nutshell_mp4-0366_jpg.rf.4e3b06e2341347a53812b60e1ff1c701.jpg: 384x640 1 nutshell, 10.9ms
image 25/568 /content/Helmet-Detector-1/test/images/Bike-Helmet-Review-VS-Nutshell_mp4-0368_jpg.rf.f08021ad1e395d0127c1ef5d50229249.jpg: 384x640 1 nutshell, 10.8ms
image 26/568 /content/Helmet-Detector-1/test/images/Bike-Helmet-Review-VS-Nutshell_mp4-0377_jpg.rf.38e5b16788d96478ddd216708d30f71d.jpg: 384x640 1 nutshell, 10.9ms
image 27/568 /content/Helmet-Detector-1/test/images/Bike-Helmet-Review-VS-Nutshell_mp4-0379_jpg.rf.1596d0e8d4842664b0d6b474f53536e8.jpg: 384x640 1 nutshell, 10.6ms
image 28/568 /content/Helmet-Detector-1/test/images/Bike-Helmet-Review-VS-Nutshell_mp4-0381_jpg.rf.9b396ed92cf2797ec2048fbb91689ef0.jpg: 384x640 1 nutshell, 14.6ms
image 29/568 /content/Helmet-Detector-1/test/images/Bike-Helmet-Review-VS-Nutshell_mp4-0389_jpg.rf.73b77d3df02924b6171bb9c1cdab2efe.jpg: 384x640 1 nutshell, 14.9ms
image 30/568 /content/Helmet-Detector-1/test/images/Bike-Helmet-Review-VS-Nutshell_mp4-0391_jpg.rf.ec0c4568563d12e8714798a6e40f16c7.jpg: 384x640 1 nutshell, 11.2ms
image 31/568 /content/Helmet-Detector-1/test/images/Bike-Helmet-Review-VS-Nutshell_mp4-0395_jpg.rf.5f027f407e414cc667feed76a3ae8fa7.jpg: 384x640 1 nutshell, 11.0ms
image 32/568 /content/Helmet-Detector-1/test/images/Bike-Helmet-Review-VS-Nutshell_mp4-0409_jpg.rf.565de87d7e68ce1c7bffe5b7c9c220e0.jpg: 384x640 1 nutshell, 10.8ms
image 33/568 /content/Helmet-Detector-1/test/images/Bike-Helmet-Review-VS-Nutshell_mp4-0586_jpg.rf.346b48f3349bb18b66eec333528e2bb4.jpg: 384x640 1 nutshell, 9.8ms
image 34/568 /content/Helmet-Detector-1/test/images/Bike-Helmet-Review-VS-Nutshell_mp4-0587_jpg.rf.f879ed210a7695d11b3794a9a607a0c2.jpg: 384x640 1 nutshell, 10.0ms
image 35/568 /content/Helmet-Detector-1/test/images/Bike-Helmet-Review-VS-Nutshell_mp4-0596_jpg.rf.bcb5c4f4854ea40dded1a0c51e955c8b.jpg: 384x640 1 nutshell, 9.9ms
image 36/568 /content/Helmet-Detector-1/test/images/Bike-Helmet-Review-VS-Nutshell_mp4-0600_jpg.rf.8931ed202829bc07c16a964c5a816552.jpg: 384x640 1 nutshell, 9.9ms
image 37/568 /content/Helmet-Detector-1/test/images/Bike-Helmet-Review-VS-Nutshell_mp4-0605_jpg.rf.e33349bd34e17624b29c734f992cbc98.jpg: 384x640 1 nutshell, 9.8ms
image 38/568 /content/Helmet-Detector-1/test/images/Bike-Helmet-Review-VS-Nutshell_mp4-0928_jpg.rf.d34186b4270faafbaf0475afef86b4b6.jpg: 384x640 1 Cycling Helmet, 10.5ms
image 39/568 /content/Helmet-Detector-1/test/images/Bike-Helmet-Review-VS-Nutshell_mp4-0929_jpg.rf.54bc9c59e538cda88eceb38e0edb2f78.jpg: 384x640 1 Cycling Helmet, 9.9ms
image 40/568 /content/Helmet-Detector-1/test/images/Bike-Helmet-Review-VS-Nutshell_mp4-0957_jpg.rf.09548a875e8de2025a1aa2095ac8ff14.jpg: 384x640 1 Cycling Helmet, 9.9ms
image 41/568 /content/Helmet-Detector-1/test/images/Bike-Helmet-Review-VS-Nutshell_mp4-1105_jpg.rf.a78d6fd436680937d85422eb69d16573.jpg: 384x640 1 nutshell, 9.9ms
image 42/568 /content/Helmet-Detector-1/test/images/Bike-Helmet-Review-VS-Nutshell_mp4-1174_jpg.rf.a6f00a7a0c48d1efc77c868a161915c4.jpg: 384x640 1 nutshell, 9.8ms
image 43/568 /content/Helmet-Detector-1/test/images/Bike-Helmet-Review-VS-Nutshell_mp4-1179_jpg.rf.bf47ccd02390a2d8339688bb015d4799.jpg: 384x640 1 nutshell, 9.7ms
image 44/568 /content/Helmet-Detector-1/test/images/Bike-Helmet-Review-VS-Nutshell_mp4-1180_jpg.rf.3c32afed8e5262cfcc790184016cd736.jpg: 384x640 1 nutshell, 9.8ms
image 45/568 /content/Helmet-Detector-1/test/images/Bike-Helmet-Review-VS-Nutshell_mp4-1181_jpg.rf.a33c7f02d58b13441d94e4e2c72a83d3.jpg: 384x640 1 nutshell, 9.8ms
image 46/568 /content/Helmet-Detector-1/test/images/Bike-Helmet-Review-VS-Nutshell_mp4-1182_jpg.rf.cd0b366c9d4410a1a54d67fe5c46581e.jpg: 384x640 1 nutshell, 10.0ms
image 47/568 /content/Helmet-Detector-1/test/images/Bike-Helmet-Review-VS-Nutshell_mp4-1184_jpg.rf.de6135cba456a5203b7d7829f1541930.jpg: 384x640 1 nutshell, 9.8ms
image 48/568 /content/Helmet-Detector-1/test/images/Change-Out-Your-Hardhat_-Safety-Shorts_mp4-0032_jpg.rf.ab021167bf9bb54e9593c8138d7882c2.jpg: 640x384 1 hard hat, 10.6ms
image 49/568 /content/Helmet-Detector-1/test/images/Change-Out-Your-Hardhat_-Safety-Shorts_mp4-0042_jpg.rf.035b9abed2c10e3eb2be7202642b7100.jpg: 640x384 1 hard hat, 9.9ms
image 50/568 /content/Helmet-Detector-1/test/images/Change-Out-Your-Hardhat_-Safety-Shorts_mp4-0088_jpg.rf.e5a7629a9f8e166ad2f9bc09cf5be348.jpg: 640x384 1 hard hat, 10.3ms
image 51/568 /content/Helmet-Detector-1/test/images/Change-Out-Your-Hardhat_-Safety-Shorts_mp4-0126_jpg.rf.13c2914fdd7f30692ca3a6486d607828.jpg: 640x384 1 hard hat, 10.1ms
image 52/568 /content/Helmet-Detector-1/test/images/Change-Out-Your-Hardhat_-Safety-Shorts_mp4-0141_jpg.rf.901cd7b0fa5b8f4c497e545bd741c38f.jpg: 640x384 1 hard hat, 9.9ms
image 53/568 /content/Helmet-Detector-1/test/images/Change-Out-Your-Hardhat_-Safety-Shorts_mp4-0181_jpg.rf.cc17225ccee861c112fae7b2bbb28ef7.jpg: 640x384 1 hard hat, 10.0ms
image 54/568 /content/Helmet-Detector-1/test/images/Change-Out-Your-Hardhat_-Safety-Shorts_mp4-0205_jpg.rf.870b3dcb17f7472275b94a1011ed3608.jpg: 640x384 1 hard hat, 11.5ms
image 55/568 /content/Helmet-Detector-1/test/images/Change-Out-Your-Hardhat_-Safety-Shorts_mp4-0211_jpg.rf.4c53650f30581e1293ca4ca3ccc3efb5.jpg: 640x384 1 hard hat, 14.5ms
image 56/568 /content/Helmet-Detector-1/test/images/Change-Out-Your-Hardhat_-Safety-Shorts_mp4-0216_jpg.rf.ddd81d5a2d526f20fdeb3864bf9b3244.jpg: 640x384 1 hard hat, 14.5ms
image 57/568 /content/Helmet-Detector-1/test/images/Change-Out-Your-Hardhat_-Safety-Shorts_mp4-0417_jpg.rf.51889e4832db3b445587b4cd4ccea105.jpg: 640x384 2 hard hats, 15.4ms
image 58/568 /content/Helmet-Detector-1/test/images/Change-Out-Your-Hardhat_-Safety-Shorts_mp4-0425_jpg.rf.74146e31b85f18cf0898d2aea2d1c5f1.jpg: 640x384 2 hard hats, 11.3ms
image 59/568 /content/Helmet-Detector-1/test/images/Change-Out-Your-Hardhat_-Safety-Shorts_mp4-0464_jpg.rf.000704c69c69bcd05859e5b43af29130.jpg: 640x384 2 hard hats, 14.5ms
image 60/568 /content/Helmet-Detector-1/test/images/Change-Out-Your-Hardhat_-Safety-Shorts_mp4-0481_jpg.rf.606e3c69473fb3a6cd86198f9dd90bbf.jpg: 640x384 2 hard hats, 14.0ms
image 61/568 /content/Helmet-Detector-1/test/images/Change-Out-Your-Hardhat_-Safety-Shorts_mp4-0590_jpg.rf.4bd8538e5aa643863748e9671b032941.jpg: 640x384 2 hard hats, 14.2ms
image 62/568 /content/Helmet-Detector-1/test/images/Get-Your-Fit-Just-Right-With-Our-Helmet-Guide-cycling-helmets_mp4-0032_jpg.rf.8ce55b6756f683d1b920fc08827e38ab.jpg: 640x384 1 Cycling Helmet, 10.8ms
image 63/568 /content/Helmet-Detector-1/test/images/Get-Your-Fit-Just-Right-With-Our-Helmet-Guide-cycling-helmets_mp4-0049_jpg.rf.40861d65fb151b925382fbd1256114ed.jpg: 640x384 1 Cycling Helmet, 15.7ms
image 64/568 /content/Helmet-Detector-1/test/images/Get-Your-Fit-Just-Right-With-Our-Helmet-Guide-cycling-helmets_mp4-0055_jpg.rf.5cc90ffd945beea292db91084a459945.jpg: 640x384 1 Cycling Helmet, 13.3ms
image 65/568 /content/Helmet-Detector-1/test/images/Get-Your-Fit-Just-Right-With-Our-Helmet-Guide-cycling-helmets_mp4-0073_jpg.rf.a90903adb01c89fa44be2b783a7ac474.jpg: 640x384 1 Cycling Helmet, 10.6ms
image 66/568 /content/Helmet-Detector-1/test/images/Get-Your-Fit-Just-Right-With-Our-Helmet-Guide-cycling-helmets_mp4-0124_jpg.rf.3bc96f41a75fcaedde6e469d616811f6.jpg: 640x384 1 Cycling Helmet, 10.8ms
image 67/568 /content/Helmet-Detector-1/test/images/Get-Your-Fit-Just-Right-With-Our-Helmet-Guide-cycling-helmets_mp4-0125_jpg.rf.3c34ee42c852dd70682fafec1ed98ad7.jpg: 640x384 1 Cycling Helmet, 14.8ms
image 68/568 /content/Helmet-Detector-1/test/images/Get-Your-Fit-Just-Right-With-Our-Helmet-Guide-cycling-helmets_mp4-0147_jpg.rf.14beac4d0a5788aa126005fb12b9abd0.jpg: 640x384 1 Cycling Helmet, 13.5ms
image 69/568 /content/Helmet-Detector-1/test/images/Get-Your-Fit-Just-Right-With-Our-Helmet-Guide-cycling-helmets_mp4-0150_jpg.rf.1af8411730343ac0396da5e0e2434192.jpg: 640x384 1 Cycling Helmet, 10.0ms
image 70/568 /content/Helmet-Detector-1/test/images/Get-Your-Fit-Just-Right-With-Our-Helmet-Guide-cycling-helmets_mp4-0169_jpg.rf.11263fb4d644d6181fb51c5b00a7928e.jpg: 640x384 1 Cycling Helmet, 10.0ms
image 71/568 /content/Helmet-Detector-1/test/images/Get-Your-Fit-Just-Right-With-Our-Helmet-Guide-cycling-helmets_mp4-0183_jpg.rf.2817a6cfaa9f62eb05afa1b85b82dc9f.jpg: 640x384 1 Cycling Helmet, 14.5ms
image 72/568 /content/Helmet-Detector-1/test/images/Get-Your-Fit-Just-Right-With-Our-Helmet-Guide-cycling-helmets_mp4-0187_jpg.rf.df10417dace989b35dfb96d68ec6cf31.jpg: 640x384 1 Cycling Helmet, 16.4ms
image 73/568 /content/Helmet-Detector-1/test/images/Get-Your-Fit-Just-Right-With-Our-Helmet-Guide-cycling-helmets_mp4-0203_jpg.rf.b19fa4934d95dd6a65c2367e377e69b0.jpg: 640x384 1 Cycling Helmet, 10.9ms
image 74/568 /content/Helmet-Detector-1/test/images/Get-Your-Fit-Just-Right-With-Our-Helmet-Guide-cycling-helmets_mp4-0205_jpg.rf.519fb58c6315196b631af98f889337b2.jpg: 640x384 1 Cycling Helmet, 13.9ms
image 75/568 /content/Helmet-Detector-1/test/images/Get-Your-Fit-Just-Right-With-Our-Helmet-Guide-cycling-helmets_mp4-0206_jpg.rf.d9e005f0899c5cab6539639043a38359.jpg: 640x384 1 Cycling Helmet, 14.1ms
image 76/568 /content/Helmet-Detector-1/test/images/Get-Your-Fit-Just-Right-With-Our-Helmet-Guide-cycling-helmets_mp4-0215_jpg.rf.48f2bff2bd1619935b92e1d1d585ea0d.jpg: 640x384 1 Cycling Helmet, 14.0ms
image 77/568 /content/Helmet-Detector-1/test/images/Get-Your-Fit-Just-Right-With-Our-Helmet-Guide-cycling-helmets_mp4-0218_jpg.rf.fb3669de77c99a006010fe0a017fdbc0.jpg: 640x384 1 Cycling Helmet, 16.4ms
image 78/568 /content/Helmet-Detector-1/test/images/Get-Your-Fit-Just-Right-With-Our-Helmet-Guide-cycling-helmets_mp4-0221_jpg.rf.a2c14d4f97718fd16358d6c3c803f71b.jpg: 640x384 1 Cycling Helmet, 11.2ms
image 79/568 /content/Helmet-Detector-1/test/images/Get-Your-Fit-Just-Right-With-Our-Helmet-Guide-cycling-helmets_mp4-0258_jpg.rf.f4e7abc2aa16a7e62457de1daf5fa4eb.jpg: 640x384 1 Cycling Helmet, 14.4ms
image 80/568 /content/Helmet-Detector-1/test/images/Get-Your-Fit-Just-Right-With-Our-Helmet-Guide-cycling-helmets_mp4-0260_jpg.rf.c30b81dff178519758446546afd28c9c.jpg: 640x384 1 Cycling Helmet, 10.7ms
image 81/568 /content/Helmet-Detector-1/test/images/Get-Your-Fit-Just-Right-With-Our-Helmet-Guide-cycling-helmets_mp4-0306_jpg.rf.0274189dc5fdba1b97821c3f9eeddd0d.jpg: 640x384 1 Cycling Helmet, 14.3ms
image 82/568 /content/Helmet-Detector-1/test/images/Get-Your-Fit-Just-Right-With-Our-Helmet-Guide-cycling-helmets_mp4-0319_jpg.rf.97f2591827871aaf2c62c224ab3ccf51.jpg: 640x384 1 Cycling Helmet, 11.7ms
image 83/568 /content/Helmet-Detector-1/test/images/Hardhats-Helmets-101_-Classification-and-ANSI-Standard-Breakdown_mp4-0018_jpg.rf.dfaaf620543988d6ffb17b846b692a31.jpg: 384x640 3 hard hats, 15.1ms
image 84/568 /content/Helmet-Detector-1/test/images/Hardhats-Helmets-101_-Classification-and-ANSI-Standard-Breakdown_mp4-0025_jpg.rf.7a573d6de3cec30864e2689ddae08065.jpg: 384x640 3 hard hats, 15.6ms
image 85/568 /content/Helmet-Detector-1/test/images/Hardhats-Helmets-101_-Classification-and-ANSI-Standard-Breakdown_mp4-0037_jpg.rf.067c059e4bc3fcff9193256edad1bc07.jpg: 384x640 1 hard hat, 20.8ms
image 86/568 /content/Helmet-Detector-1/test/images/Hardhats-Helmets-101_-Classification-and-ANSI-Standard-Breakdown_mp4-0046_jpg.rf.8f0fb2bb7ca8a05680f8df89af6e58e8.jpg: 384x640 1 hard hat, 13.0ms
image 87/568 /content/Helmet-Detector-1/test/images/Hardhats-Helmets-101_-Classification-and-ANSI-Standard-Breakdown_mp4-0048_jpg.rf.962dcb97f2abf11b635edc862cc97aeb.jpg: 384x640 1 hard hat, 13.0ms
image 88/568 /content/Helmet-Detector-1/test/images/Hardhats-Helmets-101_-Classification-and-ANSI-Standard-Breakdown_mp4-0055_jpg.rf.fc8c0cb5ebdc9c7e36969bd35aff542a.jpg: 384x640 (no detections), 13.4ms
image 89/568 /content/Helmet-Detector-1/test/images/Hardhats-Helmets-101_-Classification-and-ANSI-Standard-Breakdown_mp4-0058_jpg.rf.71d6d6437ed036bc824e24855153161c.jpg: 384x640 1 hard hat, 11.6ms
image 90/568 /content/Helmet-Detector-1/test/images/Hardhats-Helmets-101_-Classification-and-ANSI-Standard-Breakdown_mp4-0062_jpg.rf.49ee5df679989bc8ef73c1be31f78eb1.jpg: 384x640 1 hard hat, 13.1ms
image 91/568 /content/Helmet-Detector-1/test/images/Hardhats-Helmets-101_-Classification-and-ANSI-Standard-Breakdown_mp4-0073_jpg.rf.eda632ccdb80a96dc571de81907f035f.jpg: 384x640 1 hard hat, 12.6ms
image 92/568 /content/Helmet-Detector-1/test/images/Hardhats-Helmets-101_-Classification-and-ANSI-Standard-Breakdown_mp4-0078_jpg.rf.004d2717598fbd0584c4c7a505ead0ca.jpg: 384x640 1 hard hat, 12.8ms
image 93/568 /content/Helmet-Detector-1/test/images/Hardhats-Helmets-101_-Classification-and-ANSI-Standard-Breakdown_mp4-0092_jpg.rf.dc90f1128ea7eb044b192147d0b352e1.jpg: 384x640 1 hard hat, 12.6ms
image 94/568 /content/Helmet-Detector-1/test/images/Hardhats-Helmets-101_-Classification-and-ANSI-Standard-Breakdown_mp4-0112_jpg.rf.89ea2044b0e458e425d4436b0c12cd28.jpg: 384x640 1 hard hat, 11.7ms
image 95/568 /content/Helmet-Detector-1/test/images/Hardhats-Helmets-101_-Classification-and-ANSI-Standard-Breakdown_mp4-0153_jpg.rf.8636bd814d0b56446294e9d19b66fa3f.jpg: 384x640 1 hard hat, 12.8ms
image 96/568 /content/Helmet-Detector-1/test/images/Hardhats-Helmets-101_-Classification-and-ANSI-Standard-Breakdown_mp4-0157_jpg.rf.8354877c95815be169d9d071925eaf9e.jpg: 384x640 1 hard hat, 12.0ms
image 97/568 /content/Helmet-Detector-1/test/images/Hardhats-Helmets-101_-Classification-and-ANSI-Standard-Breakdown_mp4-0159_jpg.rf.4bfe7c22f51e2c75cccc33ee85301788.jpg: 384x640 1 hard hat, 12.7ms
image 98/568 /content/Helmet-Detector-1/test/images/Hardhats-Helmets-101_-Classification-and-ANSI-Standard-Breakdown_mp4-0167_jpg.rf.3f479568dda846540644a03ce2c3ba9b.jpg: 384x640 (no detections), 12.9ms
image 99/568 /content/Helmet-Detector-1/test/images/Hardhats-Helmets-101_-Classification-and-ANSI-Standard-Breakdown_mp4-0173_jpg.rf.88cc0dd72a10d4d76bc8a6ec38ea6e02.jpg: 384x640 1 hard hat, 13.0ms
image 100/568 /content/Helmet-Detector-1/test/images/Hardhats-Helmets-101_-Classification-and-ANSI-Standard-Breakdown_mp4-0181_jpg.rf.0c9db769297d47b3ab6c539e491a8159.jpg: 384x640 1 hard hat, 12.2ms
image 101/568 /content/Helmet-Detector-1/test/images/Hardhats-Helmets-101_-Classification-and-ANSI-Standard-Breakdown_mp4-0200_jpg.rf.112d57c71b67d2bbaa2f84a5298613dc.jpg: 384x640 1 hard hat, 17.3ms
image 102/568 /content/Helmet-Detector-1/test/images/Hardhats-Helmets-101_-Classification-and-ANSI-Standard-Breakdown_mp4-0208_jpg.rf.107a84b373fe6d81562c1105e7ae3670.jpg: 384x640 1 hard hat, 12.7ms
image 103/568 /content/Helmet-Detector-1/test/images/Hardhats-Helmets-101_-Classification-and-ANSI-Standard-Breakdown_mp4-0209_jpg.rf.11b0ddd0e15ac5fa4053d2f2afee2c4a.jpg: 384x640 1 hard hat, 13.1ms
image 104/568 /content/Helmet-Detector-1/test/images/Hardhats-Helmets-101_-Classification-and-ANSI-Standard-Breakdown_mp4-0214_jpg.rf.2ce194d4b2d9542ab8f08b81004eccc9.jpg: 384x640 1 hard hat, 14.1ms
image 105/568 /content/Helmet-Detector-1/test/images/Hardhats-Helmets-101_-Classification-and-ANSI-Standard-Breakdown_mp4-0255_jpg.rf.1d961473441da1d9867d130499747b87.jpg: 384x640 1 hard hat, 14.9ms
image 106/568 /content/Helmet-Detector-1/test/images/Hardhats-Helmets-101_-Classification-and-ANSI-Standard-Breakdown_mp4-0282_jpg.rf.45be63da4f67984f09bfead9628909d5.jpg: 384x640 1 hard hat, 13.7ms
image 107/568 /content/Helmet-Detector-1/test/images/Hardhats-Helmets-101_-Classification-and-ANSI-Standard-Breakdown_mp4-0290_jpg.rf.4676d21c0c17a2cf8eff8cf3d12a47fb.jpg: 384x640 1 hard hat, 13.5ms
image 108/568 /content/Helmet-Detector-1/test/images/Hardhats-Helmets-101_-Classification-and-ANSI-Standard-Breakdown_mp4-0291_jpg.rf.6d0703a068400db5aa67748ac6ada564.jpg: 384x640 1 hard hat, 13.7ms
image 109/568 /content/Helmet-Detector-1/test/images/Hardhats-Helmets-101_-Classification-and-ANSI-Standard-Breakdown_mp4-0297_jpg.rf.9887906028de2ca5601b6a3d1228ba1e.jpg: 384x640 1 hard hat, 13.7ms
image 110/568 /content/Helmet-Detector-1/test/images/Hardhats-Helmets-101_-Classification-and-ANSI-Standard-Breakdown_mp4-0302_jpg.rf.41f38f655f9f322a719e7de4283e2916.jpg: 384x640 1 hard hat, 14.1ms
image 111/568 /content/Helmet-Detector-1/test/images/Hardhats-Helmets-101_-Classification-and-ANSI-Standard-Breakdown_mp4-0319_jpg.rf.00e40d5b6bf5bad8d91530bede682ee8.jpg: 384x640 1 hard hat, 13.7ms
image 112/568 /content/Helmet-Detector-1/test/images/Hardhats-Helmets-101_-Classification-and-ANSI-Standard-Breakdown_mp4-0320_jpg.rf.3a66f6b72569e24531d1ee830dde2c49.jpg: 384x640 1 hard hat, 14.0ms
image 113/568 /content/Helmet-Detector-1/test/images/IMG_4923-1-_MOV-10_jpg.rf.62adcabe4cada989e5b5a7ecabed51bd.jpg: 640x352 1 nutshell, 62.8ms
image 114/568 /content/Helmet-Detector-1/test/images/IMG_4923-1-_MOV-19_jpg.rf.5e6289314cc73f65b5a637827aca1c72.jpg: 640x352 1 nutshell, 11.4ms
image 115/568 /content/Helmet-Detector-1/test/images/IMG_4923-1-_MOV-22_jpg.rf.5e74d5f15cdeb602c8d0e3a9c22aa54a.jpg: 640x352 1 nutshell, 7.9ms
image 116/568 /content/Helmet-Detector-1/test/images/IMG_4923-1-_MOV-24_jpg.rf.e8cb0b9bef454a08b9f1e52db6bb8aea.jpg: 640x352 1 nutshell, 7.8ms
image 117/568 /content/Helmet-Detector-1/test/images/IMG_4923-1-_MOV-28_jpg.rf.668cdfc02bd10144eac98b0851748bf1.jpg: 640x352 1 nutshell, 7.7ms
image 118/568 /content/Helmet-Detector-1/test/images/IMG_4923-1-_MOV-29_jpg.rf.ba9aaaf3ae80631ca75019f19eedb48d.jpg: 640x352 1 nutshell, 7.7ms
image 119/568 /content/Helmet-Detector-1/test/images/IMG_4923-1-_MOV-2_jpg.rf.f83780d11f3b71d71b53cdf0a372d6a3.jpg: 640x352 1 nutshell, 9.1ms
image 120/568 /content/Helmet-Detector-1/test/images/IMG_4923-1-_MOV-34_jpg.rf.a2353812adb53f70d0c5920e715f56d7.jpg: 640x352 1 nutshell, 10.4ms
image 121/568 /content/Helmet-Detector-1/test/images/IMG_4923-1-_MOV-6_jpg.rf.0e9b99eeea983c2b2a2f618091b9efb1.jpg: 640x352 1 nutshell, 12.3ms
image 122/568 /content/Helmet-Detector-1/test/images/IMG_4924_MOV-0_jpg.rf.65da7a32842180a35e3780ae89b19c3b.jpg: 640x352 1 helmet, 10.7ms
image 123/568 /content/Helmet-Detector-1/test/images/IMG_4924_MOV-10_jpg.rf.ef7d3e328d9196ed6486921dedce655d.jpg: 640x352 1 helmet, 11.8ms
image 124/568 /content/Helmet-Detector-1/test/images/IMG_4924_MOV-14_jpg.rf.b29c0804cc1c0d8ecbd94c8491d400f7.jpg: 640x352 1 helmet, 8.5ms
image 125/568 /content/Helmet-Detector-1/test/images/IMG_4924_MOV-28_jpg.rf.20c3fef1bc0e10c221e66e781ac9933b.jpg: 640x352 1 helmet, 7.8ms
image 126/568 /content/Helmet-Detector-1/test/images/IMG_4924_MOV-29_jpg.rf.fc05f8dabfef857ecffc6e4992e001b8.jpg: 640x352 1 helmet, 7.9ms
image 127/568 /content/Helmet-Detector-1/test/images/IMG_4924_MOV-30_jpg.rf.c9393ecf745ec37998389b8c9093311b.jpg: 640x352 1 helmet, 8.1ms
image 128/568 /content/Helmet-Detector-1/test/images/IMG_4996-2-_mov-0_jpg.rf.86858e4fed86aeea86a37b94197a2660.jpg: 640x352 1 plate, 7.8ms
image 129/568 /content/Helmet-Detector-1/test/images/IMG_4996-2-_mov-12_jpg.rf.977d3dde53ea066d6a87c866d8e9483d.jpg: 640x352 1 plate, 8.1ms
image 130/568 /content/Helmet-Detector-1/test/images/IMG_4996-2-_mov-13_jpg.rf.c9d2014ee98c71dd47c05d695af35386.jpg: 640x352 1 plate, 8.0ms
image 131/568 /content/Helmet-Detector-1/test/images/IMG_4996-2-_mov-14_jpg.rf.a3b5f5381f392e9cfc40ae61ffb668f6.jpg: 640x352 1 plate, 10.4ms
image 132/568 /content/Helmet-Detector-1/test/images/IMG_4996-2-_mov-16_jpg.rf.7f387a3a0df3cd25376534665113c6ea.jpg: 640x352 1 plate, 7.7ms
image 133/568 /content/Helmet-Detector-1/test/images/IMG_4996-2-_mov-21_jpg.rf.4871d27b6a14dea9ffb5e6e6d03b5d14.jpg: 640x352 1 plate, 7.7ms
image 134/568 /content/Helmet-Detector-1/test/images/IMG_4996-2-_mov-2_jpg.rf.96c0dced152e4a3948e23decf5b2c9c0.jpg: 640x352 1 plate, 7.9ms
image 135/568 /content/Helmet-Detector-1/test/images/IMG_4996-2-_mov-34_jpg.rf.e0dcc577cd967e2d4a817f6b4ee1899e.jpg: 640x352 1 plate, 11.6ms
image 136/568 /content/Helmet-Detector-1/test/images/IMG_4996-2-_mov-35_jpg.rf.de8867701da6b80d592702f8be489c86.jpg: 640x352 1 plate, 7.9ms
image 137/568 /content/Helmet-Detector-1/test/images/IMG_4996-2-_mov-39_jpg.rf.38285107e4dfab80057bf0cc28973c5e.jpg: 640x352 1 plate, 9.1ms
image 138/568 /content/Helmet-Detector-1/test/images/IMG_4996-2-_mov-40_jpg.rf.7d4a5c3e1fef189f1eaf8fe58c2ac2aa.jpg: 640x352 1 plate, 9.2ms
image 139/568 /content/Helmet-Detector-1/test/images/IMG_4996-2-_mov-41_jpg.rf.c10c20340b9f1ddf9cd593c49cfe863d.jpg: 640x352 1 plate, 7.6ms
image 140/568 /content/Helmet-Detector-1/test/images/IMG_4997-2-_mov-0_jpg.rf.ef1fd2152e8d1f9b09f45440bc9619b9.jpg: 640x352 1 plate, 7.8ms
image 141/568 /content/Helmet-Detector-1/test/images/IMG_4997-2-_mov-13_jpg.rf.1d9cf8f7f8c2325451d4fb03bcc87fef.jpg: 640x352 1 plate, 7.9ms
image 142/568 /content/Helmet-Detector-1/test/images/IMG_4997-2-_mov-22_jpg.rf.896b69f238444a660b69d753a5e7d96a.jpg: 640x352 1 plate, 7.9ms
image 143/568 /content/Helmet-Detector-1/test/images/IMG_4997-2-_mov-26_jpg.rf.2f77a2cc8ed7eeb7afc87bfa477b7aa3.jpg: 640x352 1 plate, 7.7ms
image 144/568 /content/Helmet-Detector-1/test/images/IMG_4997-2-_mov-27_jpg.rf.bf65065c672f1fa044b2cdb18b911e7a.jpg: 640x352 1 plate, 7.8ms
image 145/568 /content/Helmet-Detector-1/test/images/IMG_4997-2-_mov-28_jpg.rf.4678c4d533181a31ca3b44a387cb7293.jpg: 640x352 1 plate, 7.8ms
image 146/568 /content/Helmet-Detector-1/test/images/IMG_4997-2-_mov-2_jpg.rf.8f2f6966d870744ca2e47c85d4dd48e3.jpg: 640x352 1 plate, 7.7ms
image 147/568 /content/Helmet-Detector-1/test/images/IMG_4997-2-_mov-3_jpg.rf.ae938eb99cd0f7c2ad8ac8f2f4ea3818.jpg: 640x352 1 plate, 7.7ms
image 148/568 /content/Helmet-Detector-1/test/images/IMG_4997-2-_mov-5_jpg.rf.4e4456b9abd73d45214e1c8c36732181.jpg: 640x352 1 plate, 8.0ms
image 149/568 /content/Helmet-Detector-1/test/images/IMG_4997-2-_mov-7_jpg.rf.823b2f0fe0099aeba7e984ae41583c95.jpg: 640x352 1 plate, 7.8ms
image 150/568 /content/Helmet-Detector-1/test/images/IMG_4998-2-_mov-0_jpg.rf.07df70aaf2e12199393a8a4f692595a2.jpg: 640x352 2 plates, 7.6ms
image 151/568 /content/Helmet-Detector-1/test/images/IMG_4998-2-_mov-12_jpg.rf.2b2a061fb5376b178e9dedd1630d41f5.jpg: 640x352 1 plate, 7.6ms
image 152/568 /content/Helmet-Detector-1/test/images/IMG_4998-2-_mov-15_jpg.rf.0b16fc2d92369c7fef6523c7aa8dfbf9.jpg: 640x352 1 plate, 11.0ms
image 153/568 /content/Helmet-Detector-1/test/images/IMG_4998-2-_mov-21_jpg.rf.07297e4c721cd7005b0b0b4c217af6db.jpg: 640x352 1 plate, 7.9ms
image 154/568 /content/Helmet-Detector-1/test/images/IMG_4998-2-_mov-28_jpg.rf.9b0597e0836077144c986515502181e3.jpg: 640x352 1 plate, 7.9ms
image 155/568 /content/Helmet-Detector-1/test/images/IMG_4998-2-_mov-2_jpg.rf.fc130f6d49fbb10401140326e906d317.jpg: 640x352 2 plates, 7.6ms
image 156/568 /content/Helmet-Detector-1/test/images/IMG_4998-2-_mov-30_jpg.rf.d1940e86d22fbc40a1274c82e36741d4.jpg: 640x352 2 plates, 8.5ms
image 157/568 /content/Helmet-Detector-1/test/images/IMG_4998-2-_mov-36_jpg.rf.1462c800fd97d06712ca86ac2910b9ae.jpg: 640x352 2 plates, 7.8ms
image 158/568 /content/Helmet-Detector-1/test/images/IMG_5002_MOV-10_jpg.rf.3e4e7b53e7ae7b4ed597894070c99bf4.jpg: 640x352 1 person, 7.8ms
image 159/568 /content/Helmet-Detector-1/test/images/IMG_5002_MOV-12_jpg.rf.0d4008770228f94b4d2d17a91eb68d23.jpg: 640x352 1 person, 7.8ms
image 160/568 /content/Helmet-Detector-1/test/images/IMG_5002_MOV-2_jpg.rf.311c5d1abf044d92d6acc4a56fa47a66.jpg: 640x352 1 person, 7.7ms
image 161/568 /content/Helmet-Detector-1/test/images/IMG_5002_MOV-4_jpg.rf.7b21b599439c23d7f73019d1e8afa973.jpg: 640x352 1 person, 8.1ms
image 162/568 /content/Helmet-Detector-1/test/images/IMG_5002_MOV-7_jpg.rf.ccb5012ace244b764a3c2bef6eaf4d0e.jpg: 640x352 1 person, 8.6ms
image 163/568 /content/Helmet-Detector-1/test/images/IMG_5003_MOV-13_jpg.rf.5961f17a3ad78ef50fcabda6aa533ff9.jpg: 640x352 1 person, 7.8ms
image 164/568 /content/Helmet-Detector-1/test/images/IMG_5003_MOV-17_jpg.rf.aabdeeb7ba6a26b3a02ff8955bb9436a.jpg: 640x352 1 person, 7.7ms
image 165/568 /content/Helmet-Detector-1/test/images/IMG_5003_MOV-18_jpg.rf.b7533847eceb36d8567e41be22c190d1.jpg: 640x352 1 person, 8.1ms
image 166/568 /content/Helmet-Detector-1/test/images/IMG_5003_MOV-20_jpg.rf.5df058d19e1616f6d16c654acbb55fad.jpg: 640x352 1 person, 7.9ms
image 167/568 /content/Helmet-Detector-1/test/images/IMG_5003_MOV-23_jpg.rf.832bb9d015221666900b014b9342346c.jpg: 640x352 1 person, 7.6ms
image 168/568 /content/Helmet-Detector-1/test/images/IMG_5003_MOV-4_jpg.rf.683bb53ecab88cd4bd4708e1601f4e0b.jpg: 640x352 1 person, 7.6ms
image 169/568 /content/Helmet-Detector-1/test/images/IMG_5004_MOV-4_jpg.rf.d078064d2145bf0cfe3c6dca824b23ef.jpg: 640x352 1 person, 7.5ms
image 170/568 /content/Helmet-Detector-1/test/images/IMG_5004_MOV-6_jpg.rf.81d49846a282d198fe67f34632fa787b.jpg: 640x352 1 person, 8.1ms
image 171/568 /content/Helmet-Detector-1/test/images/IMG_5004_MOV-7_jpg.rf.c1ee30fb8f40c402d725593b08f9fb53.jpg: 640x352 1 person, 7.7ms
image 172/568 /content/Helmet-Detector-1/test/images/IMG_5006_MOV-11_jpg.rf.c3565602f00ae62e9e37ff804782496e.jpg: 640x352 1 plate, 10.9ms
image 173/568 /content/Helmet-Detector-1/test/images/IMG_5006_MOV-12_jpg.rf.593b8effd519ba5ada9db9c7e0515c21.jpg: 640x352 1 plate, 8.4ms
image 174/568 /content/Helmet-Detector-1/test/images/IMG_5006_MOV-15_jpg.rf.296be85e379e9051a799c553f3047937.jpg: 640x352 1 plate, 8.0ms
image 175/568 /content/Helmet-Detector-1/test/images/IMG_5006_MOV-16_jpg.rf.541134f545a5487b998bdac34d8c7b0d.jpg: 640x352 1 plate, 7.8ms
image 176/568 /content/Helmet-Detector-1/test/images/IMG_5006_MOV-17_jpg.rf.41ab55b85209d2a8dd982d3381081a49.jpg: 640x352 1 plate, 8.6ms
image 177/568 /content/Helmet-Detector-1/test/images/IMG_5006_MOV-19_jpg.rf.7dd4818dfcc2510b3f2a790699f92c0a.jpg: 640x352 1 plate, 7.8ms
image 178/568 /content/Helmet-Detector-1/test/images/IMG_5006_MOV-1_jpg.rf.9032e235d75cf93613f452da85f9609e.jpg: 640x352 1 plate, 7.7ms
image 179/568 /content/Helmet-Detector-1/test/images/IMG_5006_MOV-20_jpg.rf.31c1e42ac3085fa6127a5c7e30e44be5.jpg: 640x352 1 plate, 8.7ms
image 180/568 /content/Helmet-Detector-1/test/images/IMG_5006_MOV-25_jpg.rf.1631a8123837cd90b779d4b4225a0d75.jpg: 640x352 1 plate, 10.7ms
image 181/568 /content/Helmet-Detector-1/test/images/IMG_5006_MOV-27_jpg.rf.4a50ba0b43573e87fde6575279739ca4.jpg: 640x352 1 plate, 11.1ms
image 182/568 /content/Helmet-Detector-1/test/images/IMG_5006_MOV-7_jpg.rf.f4cb5fbce1b3a931dd6c1afab3619c05.jpg: 640x352 1 plate, 8.0ms
image 183/568 /content/Helmet-Detector-1/test/images/IMG_5006_MOV-8_jpg.rf.aad4761e2bbd4778aaf8422cd6175fc4.jpg: 640x352 1 plate, 7.7ms
image 184/568 /content/Helmet-Detector-1/test/images/IMG_5007_MOV-22_jpg.rf.fd91ef3c65bd76bcb45e0f571fd97ced.jpg: 640x352 1 plate, 7.7ms
image 185/568 /content/Helmet-Detector-1/test/images/IMG_5007_MOV-35_jpg.rf.cd66dad4bed90e947306616253784032.jpg: 640x352 1 plate, 8.0ms
image 186/568 /content/Helmet-Detector-1/test/images/IMG_5007_MOV-3_jpg.rf.7261e39c64022ccf87ab36f88bf37c6c.jpg: 640x352 1 plate, 7.6ms
image 187/568 /content/Helmet-Detector-1/test/images/IMG_5008_MOV-0_jpg.rf.e936a5501b52dac31c2a4f5422e81fd6.jpg: 640x352 1 helmet, 7.9ms
image 188/568 /content/Helmet-Detector-1/test/images/IMG_5008_MOV-17_jpg.rf.7068c4a2d937ae71afa043d219ed6e79.jpg: 640x352 1 helmet, 8.0ms
image 189/568 /content/Helmet-Detector-1/test/images/IMG_5008_MOV-18_jpg.rf.f55a9362e8f115936b899d938dc1950e.jpg: 640x352 1 helmet, 14.7ms
image 190/568 /content/Helmet-Detector-1/test/images/IMG_5008_MOV-5_jpg.rf.e15c5e3ed6b295e1d25fe87f64c8b9d3.jpg: 640x352 1 helmet, 8.2ms
image 191/568 /content/Helmet-Detector-1/test/images/IMG_5008_MOV-6_jpg.rf.e934409f2f4b604c428e0451f048b36c.jpg: 640x352 1 helmet, 10.2ms
image 192/568 /content/Helmet-Detector-1/test/images/IMG_5008_MOV-7_jpg.rf.9a107834a175f9dad9c35a32124fd11b.jpg: 640x352 1 helmet, 8.0ms
image 193/568 /content/Helmet-Detector-1/test/images/IMG_5011_MOV-11_jpg.rf.efba010aa84ed50878c485b4041f8729.jpg: 640x352 1 helmet, 10.2ms
image 194/568 /content/Helmet-Detector-1/test/images/IMG_5011_MOV-14_jpg.rf.e2796b78eba8a8385eae7eeb2ad05056.jpg: 640x352 1 helmet, 8.0ms
image 195/568 /content/Helmet-Detector-1/test/images/IMG_5011_MOV-17_jpg.rf.0c2fdf16f34d9e3db87b5839e37d91ff.jpg: 640x352 1 helmet, 8.0ms
image 196/568 /content/Helmet-Detector-1/test/images/IMG_5011_MOV-24_jpg.rf.660357844820d134059807453cea7f6d.jpg: 640x352 1 helmet, 7.7ms
image 197/568 /content/Helmet-Detector-1/test/images/IMG_5011_MOV-28_jpg.rf.5cee953c0766a2cc34ed7b4e66c76318.jpg: 640x352 1 helmet, 8.6ms
image 198/568 /content/Helmet-Detector-1/test/images/IMG_5011_MOV-30_jpg.rf.6735d20670a83d828c7b3e73dfea32fa.jpg: 640x352 1 helmet, 7.8ms
image 199/568 /content/Helmet-Detector-1/test/images/IMG_5011_MOV-32_jpg.rf.3aa754ec177f98d909c601d51b28dd1a.jpg: 640x352 1 helmet, 7.8ms
image 200/568 /content/Helmet-Detector-1/test/images/IMG_5011_MOV-6_jpg.rf.f028e88197b0fecddc5c374e9f36c44e.jpg: 640x352 1 helmet, 1 person, 9.4ms
image 201/568 /content/Helmet-Detector-1/test/images/IMG_5011_MOV-7_jpg.rf.18e78a693d6309e4f78d95485131c4fc.jpg: 640x352 1 helmet, 1 person, 7.9ms
image 202/568 /content/Helmet-Detector-1/test/images/IMG_5012_MOV-10_jpg.rf.795ff58b61d97d8e4708de3416a6b834.jpg: 640x352 1 motorcyclist, 8.2ms
image 203/568 /content/Helmet-Detector-1/test/images/IMG_5012_MOV-12_jpg.rf.90d09e762835d40c8d130594745c88ef.jpg: 640x352 1 motorcyclist, 8.5ms
image 204/568 /content/Helmet-Detector-1/test/images/IMG_5012_MOV-15_jpg.rf.9493896fe290243d20dc1742792d722b.jpg: 640x352 1 motorcyclist, 8.0ms
image 205/568 /content/Helmet-Detector-1/test/images/IMG_5012_MOV-18_jpg.rf.2d94ff03c00767c655b735ed3c1f734b.jpg: 640x352 1 motorcyclist, 8.3ms
image 206/568 /content/Helmet-Detector-1/test/images/IMG_5012_MOV-20_jpg.rf.51058bdb4e86264bb387d4fb9ddf473b.jpg: 640x352 1 motorcyclist, 8.1ms
image 207/568 /content/Helmet-Detector-1/test/images/IMG_5012_MOV-22_jpg.rf.32ebbdd8aedd6f0d0328bf463e75d379.jpg: 640x352 1 motorbike, 1 motorcyclist, 7.9ms
image 208/568 /content/Helmet-Detector-1/test/images/IMG_5012_MOV-23_jpg.rf.7a6987b0539fb28654c64202558db143.jpg: 640x352 1 motorbike, 1 motorcyclist, 3 persons, 7.7ms
image 209/568 /content/Helmet-Detector-1/test/images/IMG_5012_MOV-25_jpg.rf.866a5d1e68759f02f18888b0dbbdccbc.jpg: 640x352 1 motorcyclist, 4 persons, 1 plate, 7.7ms
image 210/568 /content/Helmet-Detector-1/test/images/IMG_5012_MOV-26_jpg.rf.522fbadb478bd6756e8b7b7e7893ee69.jpg: 640x352 1 motorcyclist, 4 persons, 1 plate, 11.1ms
image 211/568 /content/Helmet-Detector-1/test/images/IMG_5012_MOV-29_jpg.rf.c4c8a5541ba2c4be2e360ff81ffefd58.jpg: 640x352 1 motorcyclist, 2 persons, 1 plate, 7.6ms
image 212/568 /content/Helmet-Detector-1/test/images/IMG_5012_MOV-30_jpg.rf.8126a11cf6948c4af4238067f06c0c8b.jpg: 640x352 1 motorcyclist, 4 persons, 1 plate, 7.8ms
image 213/568 /content/Helmet-Detector-1/test/images/IMG_5012_MOV-37_jpg.rf.b22ca0735cbc2567504aec47999ee846.jpg: 640x352 1 motorcyclist, 1 plate, 7.6ms
image 214/568 /content/Helmet-Detector-1/test/images/IMG_5012_MOV-38_jpg.rf.9d3a8f9ac89b1a3dc21fe9a365918452.jpg: 640x352 1 motorcyclist, 1 plate, 7.6ms
image 215/568 /content/Helmet-Detector-1/test/images/IMG_5012_MOV-40_jpg.rf.b9e409dc47e4bd0bd7192cdeec7d0ac9.jpg: 640x352 1 motorcyclist, 7.7ms
image 216/568 /content/Helmet-Detector-1/test/images/IMG_5012_MOV-42_jpg.rf.a08308155fbbcb0c536f28d4dffeefc8.jpg: 640x352 1 motorcyclist, 9.1ms
image 217/568 /content/Helmet-Detector-1/test/images/IMG_5012_MOV-55_jpg.rf.e259fbea60fe2a97e3e7601569ed3c55.jpg: 640x352 1 motorbike, 1 motorcyclist, 7.7ms
image 218/568 /content/Helmet-Detector-1/test/images/IMG_5012_MOV-59_jpg.rf.d28769b705b9efb6d857cdee52b8dc67.jpg: 640x352 1 motorcyclist, 7.7ms
image 219/568 /content/Helmet-Detector-1/test/images/IMG_5012_MOV-9_jpg.rf.c63181598027eab1dc929f4a9085c19f.jpg: 640x352 1 motorcyclist, 8.5ms
image 220/568 /content/Helmet-Detector-1/test/images/IMG_5013_MOV-13_jpg.rf.8aad80ba380ec7b7377c69a3c1fabae8.jpg: 640x352 (no detections), 7.9ms
image 221/568 /content/Helmet-Detector-1/test/images/IMG_5013_MOV-21_jpg.rf.263f63b503398dfce7b834c5662300b8.jpg: 640x352 1 person, 8.3ms
image 222/568 /content/Helmet-Detector-1/test/images/IMG_5013_MOV-22_jpg.rf.47dfc9cf73a08bc68c1172a2be42f1f7.jpg: 640x352 1 person, 7.9ms
image 223/568 /content/Helmet-Detector-1/test/images/IMG_5013_MOV-23_jpg.rf.870bdc2b75ee3d1d9dbc9d4dee55c5a8.jpg: 640x352 1 person, 8.6ms
image 224/568 /content/Helmet-Detector-1/test/images/IMG_5013_MOV-28_jpg.rf.132edf840624cda954b6a77b4da80a46.jpg: 640x352 1 person, 8.1ms
image 225/568 /content/Helmet-Detector-1/test/images/IMG_5013_MOV-29_jpg.rf.6913890c7562de905e85d9664eb79f22.jpg: 640x352 (no detections), 8.0ms
image 226/568 /content/Helmet-Detector-1/test/images/IMG_5013_MOV-8_jpg.rf.019a1158c4ebfec1998a191c8de50690.jpg: 640x352 1 person, 8.3ms
image 227/568 /content/Helmet-Detector-1/test/images/IMG_5014_MOV-11_jpg.rf.e639af4daa34335f16153e1c240ef249.jpg: 640x352 1 person, 9.1ms
image 228/568 /content/Helmet-Detector-1/test/images/IMG_5014_MOV-12_jpg.rf.9f7751fb55c4aac05756399b0d1869fe.jpg: 640x352 1 person, 8.0ms
image 229/568 /content/Helmet-Detector-1/test/images/IMG_5014_MOV-20_jpg.rf.4983d5f088dd7764d7b57221123f9728.jpg: 640x352 1 person, 8.0ms
image 230/568 /content/Helmet-Detector-1/test/images/IMG_5014_MOV-24_jpg.rf.5401bfdc879c458ad9c66d411e8c26e2.jpg: 640x352 1 person, 7.8ms
image 231/568 /content/Helmet-Detector-1/test/images/IMG_5014_MOV-26_jpg.rf.f8377aaa26a087bce2a86080f9cad4e6.jpg: 640x352 1 person, 7.7ms
image 232/568 /content/Helmet-Detector-1/test/images/IMG_5014_MOV-27_jpg.rf.bc4e6e5334478d718d6a47a0d9088179.jpg: 640x352 1 person, 7.7ms
image 233/568 /content/Helmet-Detector-1/test/images/IMG_5014_MOV-28_jpg.rf.0a413f973920c340209919a1d8c1c141.jpg: 640x352 1 person, 7.9ms
image 234/568 /content/Helmet-Detector-1/test/images/IMG_5014_MOV-29_jpg.rf.8d149005a0d3f3bf44b2249eb8d7dbd2.jpg: 640x352 1 person, 8.3ms
image 235/568 /content/Helmet-Detector-1/test/images/IMG_5014_MOV-4_jpg.rf.d2d669b1dcfe2c73163efe4df51c00e1.jpg: 640x352 1 person, 7.7ms
image 236/568 /content/Helmet-Detector-1/test/images/IMG_5014_MOV-6_jpg.rf.5cf980ea88ecc05a215173a0ceca567f.jpg: 640x352 1 person, 8.2ms
image 237/568 /content/Helmet-Detector-1/test/images/IMG_5014_MOV-7_jpg.rf.6ecf204f492523d4090a6d85a89fb470.jpg: 640x352 1 person, 7.7ms
image 238/568 /content/Helmet-Detector-1/test/images/IMG_5015_MOV-20_jpg.rf.193c9d3b8bcff36793acc77ede52ca95.jpg: 640x352 2 persons, 7.7ms
image 239/568 /content/Helmet-Detector-1/test/images/IMG_5015_MOV-24_jpg.rf.979a8fb5c22d294fa73eb7fd9da54524.jpg: 640x352 2 persons, 7.7ms
image 240/568 /content/Helmet-Detector-1/test/images/IMG_5015_MOV-30_jpg.rf.89fd99e28ac4fd40322333e0ac6111ff.jpg: 640x352 2 persons, 7.8ms
image 241/568 /content/Helmet-Detector-1/test/images/IMG_5015_MOV-33_jpg.rf.b2b3a619e3127970349e24c7bdac41b4.jpg: 640x352 3 persons, 7.7ms
image 242/568 /content/Helmet-Detector-1/test/images/IMG_5015_MOV-34_jpg.rf.bdf82e3d7e9c614323e174b48a498786.jpg: 640x352 2 persons, 7.8ms
image 243/568 /content/Helmet-Detector-1/test/images/IMG_5015_MOV-36_jpg.rf.887c9ec60d8454260edbc6094cecfe9b.jpg: 640x352 3 persons, 9.8ms
image 244/568 /content/Helmet-Detector-1/test/images/IMG_5015_MOV-38_jpg.rf.674f13f0253ca9ca60b95fa60711c0db.jpg: 640x352 1 person, 8.4ms
image 245/568 /content/Helmet-Detector-1/test/images/IMG_5015_MOV-3_jpg.rf.d08e461d7a192644615fa6521632a0d5.jpg: 640x352 2 persons, 8.1ms
image 246/568 /content/Helmet-Detector-1/test/images/IMG_5015_MOV-44_jpg.rf.fc32549aee7ff80936a0f5288850de42.jpg: 640x352 1 person, 7.9ms
image 247/568 /content/Helmet-Detector-1/test/images/IMG_5015_MOV-4_jpg.rf.42cd7c737ac4ce6a5309e0935074c3e6.jpg: 640x352 1 person, 7.7ms
image 248/568 /content/Helmet-Detector-1/test/images/IMG_5015_MOV-51_jpg.rf.6396c11e31d32c33de1b6016f7fa7900.jpg: 640x352 1 person, 7.8ms
image 249/568 /content/Helmet-Detector-1/test/images/IMG_5015_MOV-52_jpg.rf.f32d5f5b1310fc14af27404e6030bfa0.jpg: 640x352 1 person, 10.5ms
image 250/568 /content/Helmet-Detector-1/test/images/IMG_5015_MOV-5_jpg.rf.d0dc974212ec4766fdf74dc09cf8126a.jpg: 640x352 1 person, 8.2ms
image 251/568 /content/Helmet-Detector-1/test/images/IMG_5015_MOV-6_jpg.rf.5ab0d5170fc336d6634f63e5eb6e7bc8.jpg: 640x352 2 persons, 7.8ms
image 252/568 /content/Helmet-Detector-1/test/images/IMG_5016_MOV-16_jpg.rf.0d32d8c3a46c56f03a13d7f019996db1.jpg: 640x352 3 persons, 7.7ms
image 253/568 /content/Helmet-Detector-1/test/images/IMG_5016_MOV-19_jpg.rf.90ad28dfd8aa423d1827f6e7dd55411b.jpg: 640x352 3 persons, 7.6ms
image 254/568 /content/Helmet-Detector-1/test/images/IMG_5016_MOV-21_jpg.rf.4fdfb2e3858e1461ae863684fecbcd69.jpg: 640x352 2 persons, 12.8ms
image 255/568 /content/Helmet-Detector-1/test/images/IMG_5016_MOV-22_jpg.rf.7bceb632e4a4f1a7b2f63af2fc71fb39.jpg: 640x352 2 persons, 10.6ms
image 256/568 /content/Helmet-Detector-1/test/images/IMG_5016_MOV-25_jpg.rf.edd5875f9a7e217839c33f4f1bd0b09b.jpg: 640x352 2 persons, 7.8ms
image 257/568 /content/Helmet-Detector-1/test/images/IMG_5016_MOV-29_jpg.rf.160978f81c17f6175c4d0dc6cfd64f01.jpg: 640x352 2 persons, 9.9ms
image 258/568 /content/Helmet-Detector-1/test/images/IMG_5016_MOV-2_jpg.rf.db64d717927b5bfb6b5ae5254110ea30.jpg: 640x352 3 persons, 7.8ms
image 259/568 /content/Helmet-Detector-1/test/images/IMG_5016_MOV-30_jpg.rf.f817e3a92e32af89acfc61ec5bf74214.jpg: 640x352 2 persons, 7.8ms
image 260/568 /content/Helmet-Detector-1/test/images/IMG_5016_MOV-3_jpg.rf.13058262387cd6e5a275d27c4ee1b5d5.jpg: 640x352 3 persons, 7.7ms
image 261/568 /content/Helmet-Detector-1/test/images/IMG_5016_MOV-4_jpg.rf.af376def58271970b48183cc3b14ebc2.jpg: 640x352 3 persons, 8.6ms
image 262/568 /content/Helmet-Detector-1/test/images/IMG_5031_MOV-11_jpg.rf.d2a33b353f8776c023f73d8c83adaa13.jpg: 640x352 1 person, 7.6ms
image 263/568 /content/Helmet-Detector-1/test/images/IMG_5031_MOV-12_jpg.rf.bbee31d1c43254624c035064f85c468b.jpg: 640x352 1 person, 7.6ms
image 264/568 /content/Helmet-Detector-1/test/images/IMG_5031_MOV-18_jpg.rf.aba3e210aa2f7c285995345ba19c748d.jpg: 640x352 1 person, 8.9ms
image 265/568 /content/Helmet-Detector-1/test/images/IMG_5031_MOV-19_jpg.rf.930cedb53dcdc20f1b811337b2ef2972.jpg: 640x352 1 person, 7.9ms
image 266/568 /content/Helmet-Detector-1/test/images/IMG_5031_MOV-1_jpg.rf.210713aa6bf2018d6258e1e64b815a41.jpg: 640x352 1 person, 7.8ms
image 267/568 /content/Helmet-Detector-1/test/images/IMG_5031_MOV-7_jpg.rf.875bedaaf84faf3851cfacdc2bb65cf5.jpg: 640x352 2 persons, 9.4ms
image 268/568 /content/Helmet-Detector-1/test/images/IMG_5032_MOV-10_jpg.rf.822d5e84195041f784a4885ceaef0401.jpg: 640x352 3 motorbikes, 2 plates, 8.0ms
image 269/568 /content/Helmet-Detector-1/test/images/IMG_5032_MOV-13_jpg.rf.fb19c42582229b1ffbdfbb24521e0b30.jpg: 640x352 2 motorbikes, 2 plates, 7.8ms
image 270/568 /content/Helmet-Detector-1/test/images/IMG_5032_MOV-16_jpg.rf.045ec98e5a2d8531ba574958026ae3a6.jpg: 640x352 2 motorbikes, 1 plate, 7.9ms
image 271/568 /content/Helmet-Detector-1/test/images/IMG_5032_MOV-21_jpg.rf.eaadaa890dd923c65c6ec7fca835ca53.jpg: 640x352 2 motorbikes, 3 plates, 8.2ms
image 272/568 /content/Helmet-Detector-1/test/images/IMG_5032_MOV-24_jpg.rf.4cbf74d3fe3670d61fd4f81bc4112efd.jpg: 640x352 2 motorbikes, 2 plates, 7.8ms
image 273/568 /content/Helmet-Detector-1/test/images/IMG_5032_MOV-30_jpg.rf.a0b8b826131b0b76eb30cb196157e629.jpg: 640x352 1 motorbike, 1 plate, 7.6ms
image 274/568 /content/Helmet-Detector-1/test/images/IMG_5032_MOV-7_jpg.rf.fc107afccd547c94c72eeb18ccb409e3.jpg: 640x352 4 motorbikes, 3 plates, 7.8ms
image 275/568 /content/Helmet-Detector-1/test/images/IMG_5039_MOV-16_jpg.rf.72a5ea072ac5169b06152615550ca1b5.jpg: 352x640 1 motorbike, 2 persons, 41.4ms
image 276/568 /content/Helmet-Detector-1/test/images/IMG_5039_MOV-17_jpg.rf.09a957045b0b348398a390c801bfc22a.jpg: 352x640 1 motorbike, 1 person, 8.1ms
image 277/568 /content/Helmet-Detector-1/test/images/IMG_5039_MOV-1_jpg.rf.bd996aa7f53292949c949532d7b4458c.jpg: 352x640 1 motorbike, 7.7ms
image 278/568 /content/Helmet-Detector-1/test/images/IMG_5039_MOV-20_jpg.rf.476419fd31d8af19027f4bd7e4171e09.jpg: 352x640 1 motorbike, 1 person, 8.1ms
image 279/568 /content/Helmet-Detector-1/test/images/IMG_5039_MOV-25_jpg.rf.776121fcb1d71dde355f4604b33d6e04.jpg: 352x640 1 motorbike, 1 person, 7.8ms
image 280/568 /content/Helmet-Detector-1/test/images/IMG_5039_MOV-27_jpg.rf.a7b2934190bd25e1df0325aac6f93f68.jpg: 352x640 1 motorbike, 1 plate, 8.0ms
image 281/568 /content/Helmet-Detector-1/test/images/IMG_5039_MOV-28_jpg.rf.d982a11413214bffa3f82245f6f5b8e2.jpg: 352x640 1 motorbike, 1 plate, 7.8ms
image 282/568 /content/Helmet-Detector-1/test/images/IMG_5039_MOV-29_jpg.rf.93e170b2e64073c1c5958636f5bb58e2.jpg: 352x640 1 plate, 7.9ms
image 283/568 /content/Helmet-Detector-1/test/images/IMG_5039_MOV-30_jpg.rf.361ff08fc638bb5b80699c84105525d9.jpg: 352x640 1 plate, 7.7ms
image 284/568 /content/Helmet-Detector-1/test/images/IMG_5039_MOV-37_jpg.rf.530a6e0a5fa993836cc82272162c041e.jpg: 352x640 2 plates, 8.3ms
image 285/568 /content/Helmet-Detector-1/test/images/IMG_5039_MOV-48_jpg.rf.53201b07974de493a48a04b6c41bbd6e.jpg: 352x640 1 motorbike, 1 plate, 9.0ms
image 286/568 /content/Helmet-Detector-1/test/images/IMG_5039_MOV-49_jpg.rf.d56dd0af50ac3eb7c9e3e17173bb9aa2.jpg: 352x640 1 motorbike, 1 plate, 7.7ms
image 287/568 /content/Helmet-Detector-1/test/images/IMG_5039_MOV-54_jpg.rf.892930d09da7b17779721b5c2a2e3a24.jpg: 352x640 2 motorbikes, 2 plates, 7.7ms
image 288/568 /content/Helmet-Detector-1/test/images/IMG_5039_MOV-64_jpg.rf.10d9b03dc1ca8fc4d6fb4f6725caed5a.jpg: 352x640 2 motorbikes, 7.9ms
image 289/568 /content/Helmet-Detector-1/test/images/IMG_5039_MOV-7_jpg.rf.e44d782e0339cdd0f8e712412e6e28c8.jpg: 352x640 1 motorbike, 7.8ms
image 290/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-105_jpg.rf.20bcce0914a8541fb788d705a59cb375.jpg: 640x352 1 helmet, 2 motorbikes, 1 motorcyclist, 1 person, 8.9ms
image 291/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-10_jpg.rf.2b6c93c599fdc2957ff467804ac8b018.jpg: 640x352 1 helmet, 8.6ms
image 292/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-111_jpg.rf.b8ea8813c5bed68f7d9572e6d9c21c7f.jpg: 640x352 1 helmet, 1 motorbike, 1 motorcyclist, 1 person, 7.8ms
image 293/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-112_jpg.rf.1c6463cced772f04d54aece0de3a24f8.jpg: 640x352 1 helmet, 2 motorbikes, 1 motorcyclist, 1 person, 8.2ms
image 294/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-113_jpg.rf.f846f65377a2142b4fd69e004325b4e7.jpg: 640x352 1 helmet, 2 motorbikes, 1 motorcyclist, 7.8ms
image 295/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-117_jpg.rf.e6ac53942cc046401ebd9616d1e8d764.jpg: 640x352 1 motorbike, 1 motorcyclist, 8.7ms
image 296/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-118_jpg.rf.d7cb6de51d2c5c839e38f2240d8b92f0.jpg: 640x352 1 motorbike, 1 motorcyclist, 7.7ms
image 297/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-119_jpg.rf.1b1855efbc8b801fb946a04ebc548251.jpg: 640x352 1 helmet, 1 motorbike, 1 motorcyclist, 8.1ms
image 298/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-123_jpg.rf.b9ed1462a8c13e4e5a5a1ff6e2bb883c.jpg: 640x352 3 helmets, 1 motorcyclist, 8.0ms
image 299/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-127_jpg.rf.41400c9aa4ba6d388f7f72e6789a585f.jpg: 640x352 1 helmet, 1 motorcyclist, 7.9ms
image 300/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-21_jpg.rf.e43e2339cbcbb9e6af56fb5b08844116.jpg: 640x352 1 helmet, 1 person, 7.8ms
image 301/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-24_jpg.rf.6ee7c229139fcfb41e16197a9b6f4a7d.jpg: 640x352 1 helmet, 1 motorbike, 8.2ms
image 302/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-26_jpg.rf.4fc0a3de80aef1c3370bde4fda029b46.jpg: 640x352 1 helmet, 2 motorbikes, 3 persons, 7.7ms
image 303/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-28_jpg.rf.5da8f3efe128099486bc2b87e4c7c276.jpg: 640x352 1 helmet, 2 motorbikes, 1 person, 8.6ms
image 304/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-29_jpg.rf.45f9ac316cd9e85a151c73c3946075a3.jpg: 640x352 1 helmet, 2 motorbikes, 1 person, 11.0ms
image 305/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-30_jpg.rf.2ad4d915fd8f0d55e4582bd2cce935c8.jpg: 640x352 1 helmet, 2 motorbikes, 1 person, 7.8ms
image 306/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-36_jpg.rf.1857c0b436d93d880fb1c57f4113cf6f.jpg: 640x352 1 helmet, 2 motorbikes, 1 person, 7.8ms
image 307/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-39_jpg.rf.a3c9a06cfdb9537f3f4fa18833883071.jpg: 640x352 1 helmet, 1 motorcyclist, 7.7ms
image 308/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-3_jpg.rf.31e5b248b2884fd7854006e41dd2a435.jpg: 640x352 1 helmet, 1 motorbike, 1 person, 7.7ms
image 309/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-40_jpg.rf.da3205780d4d8cc3050af92526fec1e4.jpg: 640x352 1 helmet, 1 motorcyclist, 8.9ms
image 310/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-41_jpg.rf.4d01a32cd6fcc0880fca50c403150527.jpg: 640x352 1 helmet, 1 motorbike, 7.6ms
image 311/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-43_jpg.rf.168a0e27c228eafbbb0dd74bb28abb57.jpg: 640x352 1 helmet, 1 motorbike, 1 plate, 7.6ms
image 312/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-46_jpg.rf.6ce4093f1c5219978840d50916731ce2.jpg: 640x352 1 helmet, 1 motorbike, 1 plate, 7.8ms
image 313/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-51_jpg.rf.45a95b6af07cb493bd5feb0da9331902.jpg: 640x352 1 helmet, 1 motorbike, 1 plate, 7.9ms
image 314/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-59_jpg.rf.eaa7eb5fce19b9d4000637ee992df174.jpg: 640x352 1 helmet, 1 motorbike, 1 plate, 7.7ms
image 315/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-60_jpg.rf.86bd1552c5235df803e68b040a6bb370.jpg: 640x352 1 helmet, 2 motorbikes, 1 plate, 8.1ms
image 316/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-64_jpg.rf.5707d66257b68db745afd16f5b30c3b6.jpg: 640x352 1 helmet, 3 motorbikes, 1 plate, 13.3ms
image 317/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-65_jpg.rf.d25e7fc997af96577c587c78e79250d5.jpg: 640x352 1 helmet, 2 motorbikes, 1 plate, 9.9ms
image 318/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-68_jpg.rf.c2ba93d548d80886dd0569299839f319.jpg: 640x352 1 helmet, 2 motorbikes, 1 plate, 7.8ms
image 319/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-69_jpg.rf.d92db7d2559ea8ea7aa4fed0b0e82eed.jpg: 640x352 1 helmet, 2 motorbikes, 1 plate, 7.8ms
image 320/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-73_jpg.rf.d6c82fbf571c214dd2d92e5623817330.jpg: 640x352 1 helmet, 1 plate, 14.8ms
image 321/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-75_jpg.rf.7b404e5f5c337f88676506caa39912dd.jpg: 640x352 1 helmet, 1 plate, 15.0ms
image 322/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-77_jpg.rf.25b91226628370b35967f755b3056ade.jpg: 640x352 1 helmet, 1 motorcyclist, 1 plate, 15.3ms
image 323/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-79_jpg.rf.4be4287ebac36b88f569f61746f43fba.jpg: 640x352 1 helmet, 1 motorcyclist, 1 plate, 15.5ms
image 324/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-82_jpg.rf.064f97367452477a34edb186eaf87449.jpg: 640x352 1 helmet, 1 motorbike, 1 motorcyclist, 1 plate, 10.3ms
image 325/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-83_jpg.rf.9ab6add15dba5929207e5cdd18061bfc.jpg: 640x352 1 helmet, 1 motorbike, 1 motorcyclist, 1 plate, 9.8ms
image 326/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-84_jpg.rf.2d3dcffd931c845076f31492a0db4d5e.jpg: 640x352 1 helmet, 1 motorbike, 1 motorcyclist, 1 plate, 8.7ms
image 327/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-88_jpg.rf.e9fb40244b087ccabae8962d6d1f417b.jpg: 640x352 1 helmet, 1 motorbike, 1 motorcyclist, 1 plate, 8.4ms
image 328/568 /content/Helmet-Detector-1/test/images/IMG_5040_MOV-97_jpg.rf.910c0bfd52d2eac324f4f09b9d07e48c.jpg: 640x352 1 helmet, 1 motorbike, 1 motorcyclist, 8.3ms
image 329/568 /content/Helmet-Detector-1/test/images/IMG_5041_MOV-12_jpg.rf.3eb93e2712d7965ae19d0dcd28098eed.jpg: 640x352 2 motorbikes, 1 motorcyclist, 7.7ms
image 330/568 /content/Helmet-Detector-1/test/images/IMG_5041_MOV-19_jpg.rf.6cf06b1f297f29ea113ba0e99211cf4d.jpg: 640x352 1 motorbike, 1 motorcyclist, 1 person, 8.6ms
image 331/568 /content/Helmet-Detector-1/test/images/IMG_5041_MOV-20_jpg.rf.e9694fc17ea7f069bfffd988c1c16b51.jpg: 640x352 1 motorbike, 1 person, 7.7ms
image 332/568 /content/Helmet-Detector-1/test/images/IMG_5041_MOV-24_jpg.rf.b54a92196532a42a415b34ce66e810df.jpg: 640x352 1 motorbike, 1 person, 7.7ms
image 333/568 /content/Helmet-Detector-1/test/images/IMG_5041_MOV-2_jpg.rf.6b0a7b7226ecf7cbb7419f786645c32f.jpg: 640x352 1 motorbike, 1 motorcyclist, 7.6ms
image 334/568 /content/Helmet-Detector-1/test/images/IMG_5041_MOV-32_jpg.rf.5e50de451b5bbfb63c17f4e61e598af8.jpg: 640x352 1 motorbike, 1 motorcyclist, 7.8ms
image 335/568 /content/Helmet-Detector-1/test/images/IMG_5041_MOV-35_jpg.rf.2d64022c1e7a6b79d5de7ceb53891e29.jpg: 640x352 1 motorbike, 1 person, 7.6ms
image 336/568 /content/Helmet-Detector-1/test/images/IMG_5041_MOV-3_jpg.rf.c68df1f56715a3c14a0f8450099d857a.jpg: 640x352 1 motorcyclist, 7.9ms
image 337/568 /content/Helmet-Detector-1/test/images/IMG_5041_MOV-41_jpg.rf.770f9fb9cbf101d16a468a53197e1936.jpg: 640x352 1 motorbike, 1 person, 1 plate, 10.0ms
image 338/568 /content/Helmet-Detector-1/test/images/IMG_5041_MOV-49_jpg.rf.c7451bd6e2fcf0a9cdb9a93c2f7f68b7.jpg: 640x352 1 plate, 7.8ms
image 339/568 /content/Helmet-Detector-1/test/images/IMG_5041_MOV-54_jpg.rf.d46deb2a6ed68c39ddbb1e5bda192e65.jpg: 640x352 1 motorbike, 1 plate, 7.7ms
image 340/568 /content/Helmet-Detector-1/test/images/IMG_5041_MOV-55_jpg.rf.084d674c318060f4f4d688914465a7c7.jpg: 640x352 1 motorbike, 1 plate, 7.8ms
image 341/568 /content/Helmet-Detector-1/test/images/IMG_5041_MOV-64_jpg.rf.e78500105f02c2c89a4f99df5660e453.jpg: 640x352 1 motorbike, 1 plate, 7.7ms
image 342/568 /content/Helmet-Detector-1/test/images/IMG_5041_MOV-66_jpg.rf.a3ee75d01da22d73fba28a4d1ec2a484.jpg: 640x352 1 motorbike, 1 plate, 7.6ms
image 343/568 /content/Helmet-Detector-1/test/images/IMG_5041_MOV-69_jpg.rf.faea615893efa4c3b250e89775b3e3ca.jpg: 640x352 1 motorbike, 1 motorcyclist, 1 plate, 8.1ms
image 344/568 /content/Helmet-Detector-1/test/images/IMG_5041_MOV-77_jpg.rf.237384006fee916251ee82dbc3ce98d6.jpg: 640x352 1 motorbike, 1 person, 7.7ms
image 345/568 /content/Helmet-Detector-1/test/images/IMG_5041_MOV-83_jpg.rf.c0368a3bbae2af4753eeebc69fc3b326.jpg: 640x352 1 motorbike, 1 person, 7.9ms
image 346/568 /content/Helmet-Detector-1/test/images/IMG_5041_MOV-86_jpg.rf.c990df923e75715390196b63af2097b0.jpg: 640x352 1 motorbike, 1 person, 7.7ms
image 347/568 /content/Helmet-Detector-1/test/images/IMG_5041_MOV-88_jpg.rf.63b5e195b82def268c3d089ae3b55bf9.jpg: 640x352 1 motorbike, 1 person, 7.9ms
image 348/568 /content/Helmet-Detector-1/test/images/IMG_5041_MOV-89_jpg.rf.97285f52e485db01f03e4cdf7d8a01c7.jpg: 640x352 1 motorbike, 1 person, 8.0ms
image 349/568 /content/Helmet-Detector-1/test/images/IMG_5041_MOV-92_jpg.rf.a0fd18d0762d7a4ffefaded7f573fc0e.jpg: 640x352 1 motorbike, 1 person, 7.9ms
image 350/568 /content/Helmet-Detector-1/test/images/IMG_5041_MOV-97_jpg.rf.b929b1947123fba3e68492e05e91e03d.jpg: 640x352 1 motorbike, 1 person, 7.7ms
image 351/568 /content/Helmet-Detector-1/test/images/JPX-Half-Face-Helmet-helmet-motorcycle_mp4-0002_jpg.rf.b076950ebc59de5869ddba271b9d0520.jpg: 640x384 1 half face, 8.3ms
image 352/568 /content/Helmet-Detector-1/test/images/JPX-Half-Face-Helmet-helmet-motorcycle_mp4-0005_jpg.rf.de99bb45124df4a1673702873f84dea2.jpg: 640x384 1 half face, 8.1ms
image 353/568 /content/Helmet-Detector-1/test/images/JPX-Half-Face-Helmet-helmet-motorcycle_mp4-0034_jpg.rf.533092e4836196ea2f594be1c61678c2.jpg: 640x384 1 half face, 7.8ms
image 354/568 /content/Helmet-Detector-1/test/images/JPX-Half-Face-Helmet-helmet-motorcycle_mp4-0067_jpg.rf.6c0c169bd06fe9efc4bb2723fa56de1a.jpg: 640x384 1 half face, 8.4ms
image 355/568 /content/Helmet-Detector-1/test/images/JPX-Half-Face-Helmet-helmet-motorcycle_mp4-0068_jpg.rf.004439c20423df38facb52a9bfaa4c80.jpg: 640x384 1 half face, 12.5ms
image 356/568 /content/Helmet-Detector-1/test/images/JPX-Half-Face-Helmet-helmet-motorcycle_mp4-0069_jpg.rf.ad675cda081f4a4ae4d5886fb6108265.jpg: 640x384 1 half face, 8.0ms
image 357/568 /content/Helmet-Detector-1/test/images/JPX-Half-Face-Helmet-helmet-motorcycle_mp4-0071_jpg.rf.a0956752485c3347d16dd4780bf3ffb3.jpg: 640x384 1 half face, 8.9ms
image 358/568 /content/Helmet-Detector-1/test/images/JPX-Half-Face-Helmet-helmet-motorcycle_mp4-0072_jpg.rf.df4dbaf25ba6b34a6212fc8ded2f2d82.jpg: 640x384 1 half face, 7.8ms
image 359/568 /content/Helmet-Detector-1/test/images/JPX-Half-Face-Helmet-helmet-motorcycle_mp4-0081_jpg.rf.02ac87840c4bcc6aea31c56d38d2bf3e.jpg: 640x384 1 half face, 8.0ms
image 360/568 /content/Helmet-Detector-1/test/images/JPX-Half-Face-Helmet-helmet-motorcycle_mp4-0086_jpg.rf.ce7700700ac027b63693c9f32372ab8c.jpg: 640x384 1 half face, 8.3ms
image 361/568 /content/Helmet-Detector-1/test/images/JPX-Half-Face-Helmet-helmet-motorcycle_mp4-0089_jpg.rf.db281cae5211739060c96bc808f296fc.jpg: 640x384 1 half face, 7.8ms
image 362/568 /content/Helmet-Detector-1/test/images/JPX-Half-Face-Helmet-helmet-motorcycle_mp4-0116_jpg.rf.7269912de182ad95b9fbb8df38e6eeb9.jpg: 640x384 1 half face, 8.2ms
image 363/568 /content/Helmet-Detector-1/test/images/JPX-Half-Face-Helmet-helmet-motorcycle_mp4-0121_jpg.rf.60a93a9f05345a4e2ced9675a83184b9.jpg: 640x384 1 half face, 7.7ms
image 364/568 /content/Helmet-Detector-1/test/images/JPX-Half-Face-Helmet-helmet-motorcycle_mp4-0144_jpg.rf.624566749e6d357961fafbd0bdddd5c0.jpg: 640x384 1 half face, 11.7ms
image 365/568 /content/Helmet-Detector-1/test/images/JPX-Half-Face-Helmet-helmet-motorcycle_mp4-0154_jpg.rf.96d8bfb4d7e124a8f5036d58f030baf9.jpg: 640x384 1 half face, 9.8ms
image 366/568 /content/Helmet-Detector-1/test/images/JPX-Half-Face-Helmet-helmet-motorcycle_mp4-0168_jpg.rf.17ca3cbe6c39e83d114051bde8aff5d1.jpg: 640x384 1 half face, 8.1ms
image 367/568 /content/Helmet-Detector-1/test/images/JPX-Half-Face-Helmet-helmet-motorcycle_mp4-0179_jpg.rf.21e1a3e5cf29b92a48411fbbbfbbae64.jpg: 640x384 1 half face, 7.7ms
image 368/568 /content/Helmet-Detector-1/test/images/JPX-Half-Face-Helmet-helmet-motorcycle_mp4-0194_jpg.rf.5ab33d1c6a5033adeeaf270ba4eff46b.jpg: 640x384 1 half face, 8.0ms
image 369/568 /content/Helmet-Detector-1/test/images/JPX-Half-Face-Helmet-helmet-motorcycle_mp4-0197_jpg.rf.9a76199423a5cb312a2410751ea1f107.jpg: 640x384 1 half face, 8.0ms
image 370/568 /content/Helmet-Detector-1/test/images/JPX-Half-Face-Helmet-helmet-motorcycle_mp4-0200_jpg.rf.bb06b86daf00254aeadc28a59f2c4646.jpg: 640x384 1 half face, 7.7ms
image 371/568 /content/Helmet-Detector-1/test/images/JPX-Half-Face-Helmet-helmet-motorcycle_mp4-0206_jpg.rf.368a0b399115270b69c69f67b7ffe498.jpg: 640x384 1 half face, 8.0ms
image 372/568 /content/Helmet-Detector-1/test/images/JPX-Half-Face-Helmet-helmet-motorcycle_mp4-0210_jpg.rf.aafc881db528254a805258207787dab7.jpg: 640x384 1 half face, 7.7ms
image 373/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0008_jpg.rf.3507754c5fdd28181cf3f5f79fee7eed.jpg: 640x384 1 helmet, 7.7ms
image 374/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0009_jpg.rf.0aa9b3be7b67d448a15a44ccf9525e5b.jpg: 640x384 1 helmet, 7.7ms
image 375/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0015_jpg.rf.1ade99e09c43856f9b1158a3430f7b72.jpg: 640x384 1 helmet, 7.7ms
image 376/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0021_jpg.rf.4db90346bd56993202c39846a857fab5.jpg: 640x384 1 helmet, 7.9ms
image 377/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0032_jpg.rf.ecb01b25b490f646f4522601de309e89.jpg: 640x384 2 helmets, 7.7ms
image 378/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0049_jpg.rf.e375f965b2c4564f13e88a1007458b4b.jpg: 640x384 2 helmets, 8.3ms
image 379/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0056_jpg.rf.5e5b01bc0d22e85835f2ca6c9f6d9491.jpg: 640x384 1 helmet, 10.3ms
image 380/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0062_jpg.rf.f5c73d2b4d58ab1b5e56b4c7512b31b1.jpg: 640x384 1 helmet, 7.8ms
image 381/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0066_jpg.rf.e722c4cb9890a12baa7343b178d876e6.jpg: 640x384 1 helmet, 12.1ms
image 382/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0074_jpg.rf.5db50714778ef594c2803688736a3ec3.jpg: 640x384 1 helmet, 13.3ms
image 383/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0082_jpg.rf.a36a85f7b71504368e1494177bd3f276.jpg: 640x384 1 helmet, 8.1ms
image 384/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0094_jpg.rf.8c8a94aee478b7efa28b1defd56d249c.jpg: 640x384 1 helmet, 7.8ms
image 385/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0098_jpg.rf.22f261b2ca1f15e7f3e4dfb6f129ab0f.jpg: 640x384 1 helmet, 7.7ms
image 386/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0101_jpg.rf.426051345e57659182bd9920b317232c.jpg: 640x384 1 helmet, 8.3ms
image 387/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0108_jpg.rf.574463dadaae0cee3def78ac0ccb133b.jpg: 640x384 1 helmet, 11.2ms
image 388/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0114_jpg.rf.9e1d92ec0fb0c342060bdfa2e47a5a36.jpg: 640x384 1 helmet, 8.2ms
image 389/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0116_jpg.rf.aa8af66ddb12a63c26200959dbe9123d.jpg: 640x384 1 helmet, 8.9ms
image 390/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0118_jpg.rf.0dabe9780985cd47c480b6f1b6eb1c9b.jpg: 640x384 1 helmet, 8.1ms
image 391/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0121_jpg.rf.4db8815a9b2d4a3c9515ed9d418fa4b7.jpg: 640x384 1 helmet, 8.0ms
image 392/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0124_jpg.rf.a6a2c1d41b0c2304b60bc0c77df5cfdb.jpg: 640x384 1 helmet, 7.8ms
image 393/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0127_jpg.rf.6590b5593f2ab563f8a0620bd024b687.jpg: 640x384 1 helmet, 10.8ms
image 394/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0129_jpg.rf.410a40643e18c9f60055eacf7a512fd8.jpg: 640x384 1 helmet, 8.1ms
image 395/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0134_jpg.rf.9ea8a9ecd780b02ddfe80da52060a4c1.jpg: 640x384 1 helmet, 7.9ms
image 396/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0135_jpg.rf.1a4d96044397b439ff3636e883f13bf7.jpg: 640x384 1 helmet, 8.0ms
image 397/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0136_jpg.rf.431da7ab4ea87242bd99c7ee2ea4778c.jpg: 640x384 1 helmet, 7.9ms
image 398/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0138_jpg.rf.7c9f81d2bea9fb67fe07478b81ac9eb3.jpg: 640x384 1 helmet, 7.9ms
image 399/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0147_jpg.rf.d4d5463aa72a0e12c18d59ebaefac5e0.jpg: 640x384 1 helmet, 7.8ms
image 400/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0154_jpg.rf.0210a1d8d362c8cc7b6dac22b5f65553.jpg: 640x384 1 helmet, 8.0ms
image 401/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0162_jpg.rf.5b5f755857e6c1ae6b9440f298d5db96.jpg: 640x384 1 helmet, 7.9ms
image 402/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0164_jpg.rf.3b40762a19c87d92c88d5b2f8b714fa7.jpg: 640x384 1 helmet, 11.2ms
image 403/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0169_jpg.rf.e6a1de1b2284ce93cdcaa6b6eb0bc25e.jpg: 640x384 1 helmet, 7.8ms
image 404/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0170_jpg.rf.c39fac6684e06b3bd0adda6a866c8b8a.jpg: 640x384 1 helmet, 7.9ms
image 405/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0181_jpg.rf.ed8a33fb0f54b011f68209a693619446.jpg: 640x384 1 helmet, 7.7ms
image 406/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0220_jpg.rf.0bbf6a2141c2cc55cfee92d2fbc9a19d.jpg: 640x384 1 Cycling Helmet, 1 helmet, 7.8ms
image 407/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0226_jpg.rf.833427c904189e5a3ee5defc284afd09.jpg: 640x384 1 helmet, 7.6ms
image 408/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0230_jpg.rf.322930dfe64ce3bed53483ad77dde138.jpg: 640x384 1 helmet, 7.6ms
image 409/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0232_jpg.rf.61600a6ef34a360610cfa2aaba929d36.jpg: 640x384 1 helmet, 7.8ms
image 410/568 /content/Helmet-Detector-1/test/images/Motorhelmets-Shoei-X-fourteen-Aerodyne-TC-4-Full-Face-Helmet-Racing-Motorcycle-Helmet-shorts_mp4-0268_jpg.rf.d90c7f070f24cffd7589ebfad24ba7d4.jpg: 640x384 1 helmet, 8.2ms
image 411/568 /content/Helmet-Detector-1/test/images/Pros-and-cons-ng-modular-helmet_mp4-0005_jpg.rf.659aaa46bb14c5ee760b5fa7560fb07e.jpg: 384x640 1 helmet, 8.4ms
image 412/568 /content/Helmet-Detector-1/test/images/Pros-and-cons-ng-modular-helmet_mp4-0018_jpg.rf.5ec60a64dafa255b427a566cc6e26267.jpg: 384x640 1 helmet, 8.0ms
image 413/568 /content/Helmet-Detector-1/test/images/Pros-and-cons-ng-modular-helmet_mp4-0020_jpg.rf.b4d01e2fe7e82892c83cf97d70d7d3fd.jpg: 384x640 1 helmet, 8.1ms
image 414/568 /content/Helmet-Detector-1/test/images/Pros-and-cons-ng-modular-helmet_mp4-0041_jpg.rf.0bf760550e3599d38276c49696d63fce.jpg: 384x640 1 helmet, 7.8ms
image 415/568 /content/Helmet-Detector-1/test/images/Pros-and-cons-ng-modular-helmet_mp4-0056_jpg.rf.8b9ee1ffde82a6881410e70e6faf0293.jpg: 384x640 1 helmet, 7.8ms
image 416/568 /content/Helmet-Detector-1/test/images/Pros-and-cons-ng-modular-helmet_mp4-0074_jpg.rf.fb12a215cd4f1ccb09a52fbf7ccda55f.jpg: 384x640 1 helmet, 7.8ms
image 417/568 /content/Helmet-Detector-1/test/images/Pros-and-cons-ng-modular-helmet_mp4-0098_jpg.rf.83e89677d57f3f22cd621001d2852516.jpg: 384x640 1 helmet, 7.8ms
image 418/568 /content/Helmet-Detector-1/test/images/Pros-and-cons-ng-modular-helmet_mp4-0099_jpg.rf.d08dd2887f2e1f84c7f1e1cdca3424c5.jpg: 384x640 1 helmet, 7.7ms
image 419/568 /content/Helmet-Detector-1/test/images/Pros-and-cons-ng-modular-helmet_mp4-0127_jpg.rf.31eee7f65f80772b09d180e6262713fa.jpg: 384x640 1 modular helmet, 7.7ms
image 420/568 /content/Helmet-Detector-1/test/images/Pros-and-cons-ng-modular-helmet_mp4-0148_jpg.rf.00b1a4e48c1d9d26e7cb8f6fc50ffefd.jpg: 384x640 1 modular helmet, 7.9ms
image 421/568 /content/Helmet-Detector-1/test/images/Pros-and-cons-ng-modular-helmet_mp4-0150_jpg.rf.e62a915a8460009e9f2bccd5eff15231.jpg: 384x640 1 modular helmet, 8.3ms
image 422/568 /content/Helmet-Detector-1/test/images/Pros-and-cons-ng-modular-helmet_mp4-0162_jpg.rf.317fbed08134ebe2cca0c45d47d75361.jpg: 384x640 1 modular helmet, 11.9ms
image 423/568 /content/Helmet-Detector-1/test/images/Pros-and-cons-ng-modular-helmet_mp4-0297_jpg.rf.b7fe2d2a338bbdcc3dbe8f4840d45203.jpg: 384x640 1 modular helmet, 8.2ms
image 424/568 /content/Helmet-Detector-1/test/images/Pros-and-cons-ng-modular-helmet_mp4-0311_jpg.rf.4b00e42a6f9228f965b3bdb9e0470836.jpg: 384x640 1 modular helmet, 7.9ms
image 425/568 /content/Helmet-Detector-1/test/images/Pros-and-cons-ng-modular-helmet_mp4-0329_jpg.rf.8b40faab8abddc6935bf5256b2ab50ef.jpg: 384x640 1 modular helmet, 11.0ms
image 426/568 /content/Helmet-Detector-1/test/images/Pros-and-cons-ng-modular-helmet_mp4-0360_jpg.rf.71bb218284ea686f645031307dbd266c.jpg: 384x640 1 modular helmet, 7.7ms
image 427/568 /content/Helmet-Detector-1/test/images/Pros-and-cons-ng-modular-helmet_mp4-0378_jpg.rf.bd333cbb5e778aba067936415ea02711.jpg: 384x640 1 modular helmet, 7.7ms
image 428/568 /content/Helmet-Detector-1/test/images/Pros-and-cons-ng-modular-helmet_mp4-0383_jpg.rf.aa682f06e04b829c8276cfec642df373.jpg: 384x640 1 modular helmet, 7.5ms
image 429/568 /content/Helmet-Detector-1/test/images/Pros-and-cons-ng-modular-helmet_mp4-0385_jpg.rf.12867b6ae0af829ec67d58f639e6c035.jpg: 384x640 1 modular helmet, 8.1ms
image 430/568 /content/Helmet-Detector-1/test/images/Pros-and-cons-ng-modular-helmet_mp4-0409_jpg.rf.6a26f9350b6b7b37307e6b150109f19d.jpg: 384x640 1 modular helmet, 7.7ms
image 431/568 /content/Helmet-Detector-1/test/images/Pros-and-cons-ng-modular-helmet_mp4-0442_jpg.rf.7e26c7420f5d5e21555aeae85ce1bb10.jpg: 384x640 1 modular helmet, 7.6ms
image 432/568 /content/Helmet-Detector-1/test/images/Pros-and-cons-ng-modular-helmet_mp4-0443_jpg.rf.aaed84c2096f6860620c8df76049a83c.jpg: 384x640 1 modular helmet, 8.2ms
image 433/568 /content/Helmet-Detector-1/test/images/Pros-and-cons-ng-modular-helmet_mp4-0454_jpg.rf.e78fe8ad8208e3a27a954967fc9df752.jpg: 384x640 1 modular helmet, 7.6ms
image 434/568 /content/Helmet-Detector-1/test/images/Pros-and-cons-ng-modular-helmet_mp4-0461_jpg.rf.29246ce799296344e35989105d07c0a5.jpg: 384x640 1 modular helmet, 7.8ms
image 435/568 /content/Helmet-Detector-1/test/images/Pros-and-cons-ng-modular-helmet_mp4-0463_jpg.rf.78386d8404311d767e37855df46e803e.jpg: 384x640 1 modular helmet, 7.5ms
image 436/568 /content/Helmet-Detector-1/test/images/Pros-and-cons-ng-modular-helmet_mp4-0506_jpg.rf.43bc504c66a905b3e413b4d00682d745.jpg: 384x640 1 modular helmet, 8.0ms
image 437/568 /content/Helmet-Detector-1/test/images/Pros-and-cons-ng-modular-helmet_mp4-0521_jpg.rf.5b754f6fe1f28faa08487b9496a7fd37.jpg: 384x640 1 modular helmet, 7.7ms
image 438/568 /content/Helmet-Detector-1/test/images/Pros-and-cons-ng-modular-helmet_mp4-0527_jpg.rf.a5c7e806831f3d85307558e9990a53a5.jpg: 384x640 1 helmet, 7.7ms
image 439/568 /content/Helmet-Detector-1/test/images/Pros-and-cons-ng-modular-helmet_mp4-0577_jpg.rf.e92b23a7c683399e8a8fa515b28fdbea.jpg: 384x640 1 helmet, 7.7ms
image 440/568 /content/Helmet-Detector-1/test/images/Pros-and-cons-ng-modular-helmet_mp4-0643_jpg.rf.f49f4673d47f9e513b09d35925916684.jpg: 384x640 1 helmet, 10.9ms
image 441/568 /content/Helmet-Detector-1/test/images/Pros-and-cons-ng-modular-helmet_mp4-0648_jpg.rf.02dd10af28c8acd445491ffd87785fa7.jpg: 384x640 1 helmet, 7.8ms
image 442/568 /content/Helmet-Detector-1/test/images/Pros-and-cons-ng-modular-helmet_mp4-0652_jpg.rf.d8e55fe4224a0d41d1cc544cb7c946d2.jpg: 384x640 1 helmet, 7.8ms
image 443/568 /content/Helmet-Detector-1/test/images/Pros-and-cons-ng-modular-helmet_mp4-0663_jpg.rf.5503c2fc98a21f2da9f88ed514f998cd.jpg: 384x640 1 helmet, 7.7ms
image 444/568 /content/Helmet-Detector-1/test/images/Pros-and-cons-ng-modular-helmet_mp4-0679_jpg.rf.8e67accc8e567a76e20a19e204475867.jpg: 384x640 1 helmet, 7.6ms
image 445/568 /content/Helmet-Detector-1/test/images/Pros-and-cons-ng-modular-helmet_mp4-0688_jpg.rf.23d2af95ee0f46734d7a29fdafef9a13.jpg: 384x640 1 helmet, 7.8ms
image 446/568 /content/Helmet-Detector-1/test/images/Quality-Affordable-Cycling-Helmet-Eyewear-Jersey-from-teamspyderphils-_mp4-0057_jpg.rf.373c2cc491456f8f07a6c3916faf7c82.jpg: 640x384 1 Cycling Helmet, 8.5ms
image 447/568 /content/Helmet-Detector-1/test/images/Quality-Affordable-Cycling-Helmet-Eyewear-Jersey-from-teamspyderphils-_mp4-0066_jpg.rf.fef84afbf53bbb95c2efcad96a89e5e1.jpg: 640x384 1 Cycling Helmet, 8.2ms
image 448/568 /content/Helmet-Detector-1/test/images/Quality-Affordable-Cycling-Helmet-Eyewear-Jersey-from-teamspyderphils-_mp4-0069_jpg.rf.c7b6d7e24d6df748d6e6970a660360c4.jpg: 640x384 1 Cycling Helmet, 7.9ms
image 449/568 /content/Helmet-Detector-1/test/images/Quality-Affordable-Cycling-Helmet-Eyewear-Jersey-from-teamspyderphils-_mp4-0072_jpg.rf.b19c3e268aeb5f1ec88b19cb3d7f6fd7.jpg: 640x384 1 Cycling Helmet, 7.7ms
image 450/568 /content/Helmet-Detector-1/test/images/Quality-Affordable-Cycling-Helmet-Eyewear-Jersey-from-teamspyderphils-_mp4-0073_jpg.rf.84412bce949651129c209223ea334a5e.jpg: 640x384 1 Cycling Helmet, 7.7ms
image 451/568 /content/Helmet-Detector-1/test/images/Quality-Affordable-Cycling-Helmet-Eyewear-Jersey-from-teamspyderphils-_mp4-0208_jpg.rf.2fe56f080bc472b25afd6f4a7de45970.jpg: 640x384 1 Cycling Helmet, 8.4ms
image 452/568 /content/Helmet-Detector-1/test/images/Quality-Affordable-Cycling-Helmet-Eyewear-Jersey-from-teamspyderphils-_mp4-0209_jpg.rf.99669c59923119fb1f09c234a42be082.jpg: 640x384 1 Cycling Helmet, 8.0ms
image 453/568 /content/Helmet-Detector-1/test/images/Quality-Affordable-Cycling-Helmet-Eyewear-Jersey-from-teamspyderphils-_mp4-0218_jpg.rf.9c2841ed593bfa7cd2c3a83a5ce2a9af.jpg: 640x384 1 Cycling Helmet, 7.8ms
image 454/568 /content/Helmet-Detector-1/test/images/Quality-Affordable-Cycling-Helmet-Eyewear-Jersey-from-teamspyderphils-_mp4-0224_jpg.rf.3c9c44e90a139b4aa465c429a2d43ad0.jpg: 640x384 1 Cycling Helmet, 7.6ms
image 455/568 /content/Helmet-Detector-1/test/images/Quality-Affordable-Cycling-Helmet-Eyewear-Jersey-from-teamspyderphils-_mp4-0232_jpg.rf.b8db074521616f660eb7c9de38394c15.jpg: 640x384 1 Cycling Helmet, 8.2ms
image 456/568 /content/Helmet-Detector-1/test/images/Quality-Affordable-Cycling-Helmet-Eyewear-Jersey-from-teamspyderphils-_mp4-0233_jpg.rf.abe180ba0274cdc54ba8e0c254ad120e.jpg: 640x384 1 Cycling Helmet, 10.0ms
image 457/568 /content/Helmet-Detector-1/test/images/Quality-Affordable-Cycling-Helmet-Eyewear-Jersey-from-teamspyderphils-_mp4-0245_jpg.rf.a8e363c587f199ef9ebe1344a216f548.jpg: 640x384 1 Cycling Helmet, 7.8ms
image 458/568 /content/Helmet-Detector-1/test/images/Quality-Affordable-Cycling-Helmet-Eyewear-Jersey-from-teamspyderphils-_mp4-0255_jpg.rf.b897ddef079b65829e96d1331841b72c.jpg: 640x384 1 Cycling Helmet, 11.5ms
image 459/568 /content/Helmet-Detector-1/test/images/Quality-Affordable-Cycling-Helmet-Eyewear-Jersey-from-teamspyderphils-_mp4-0260_jpg.rf.7a1b820b4722d53357bf3d88f4c886b4.jpg: 640x384 1 Cycling Helmet, 12.9ms
image 460/568 /content/Helmet-Detector-1/test/images/Quality-Affordable-Cycling-Helmet-Eyewear-Jersey-from-teamspyderphils-_mp4-0268_jpg.rf.f47d0c17bdea64d0b61b529b986b9c65.jpg: 640x384 1 Cycling Helmet, 7.8ms
image 461/568 /content/Helmet-Detector-1/test/images/Quality-Affordable-Cycling-Helmet-Eyewear-Jersey-from-teamspyderphils-_mp4-0269_jpg.rf.9021d16742a1be645fab03085d7f48e7.jpg: 640x384 1 Cycling Helmet, 7.7ms
image 462/568 /content/Helmet-Detector-1/test/images/Quality-Affordable-Cycling-Helmet-Eyewear-Jersey-from-teamspyderphils-_mp4-0273_jpg.rf.4437dc22c6c3881e93afc62923b41b84.jpg: 640x384 1 Cycling Helmet, 11.5ms
image 463/568 /content/Helmet-Detector-1/test/images/Quality-Affordable-Cycling-Helmet-Eyewear-Jersey-from-teamspyderphils-_mp4-0291_jpg.rf.2c107b004589d2604b3e58e66f5d9eea.jpg: 640x384 1 Cycling Helmet, 8.3ms
image 464/568 /content/Helmet-Detector-1/test/images/Quality-Affordable-Cycling-Helmet-Eyewear-Jersey-from-teamspyderphils-_mp4-0294_jpg.rf.0cdf186650728c462b9c1cb6d52a903c.jpg: 640x384 1 Cycling Helmet, 7.9ms
image 465/568 /content/Helmet-Detector-1/test/images/Quality-Affordable-Cycling-Helmet-Eyewear-Jersey-from-teamspyderphils-_mp4-0295_jpg.rf.49bab288d82e8c7ccc8cdd3c71fff241.jpg: 640x384 1 Cycling Helmet, 7.9ms
image 466/568 /content/Helmet-Detector-1/test/images/Quality-Affordable-Cycling-Helmet-Eyewear-Jersey-from-teamspyderphils-_mp4-0315_jpg.rf.cf9814f9f73391d754732709cccfa279.jpg: 640x384 1 Cycling Helmet, 8.1ms
image 467/568 /content/Helmet-Detector-1/test/images/Quality-Affordable-Cycling-Helmet-Eyewear-Jersey-from-teamspyderphils-_mp4-0316_jpg.rf.f25a5f0016faa1d9bfff90d6d76f9946.jpg: 640x384 1 Cycling Helmet, 7.8ms
image 468/568 /content/Helmet-Detector-1/test/images/Quality-Affordable-Cycling-Helmet-Eyewear-Jersey-from-teamspyderphils-_mp4-0320_jpg.rf.43deeb71d0835b95f6bb8b42e8cf22ea.jpg: 640x384 1 Cycling Helmet, 8.1ms
image 469/568 /content/Helmet-Detector-1/test/images/Quality-Affordable-Cycling-Helmet-Eyewear-Jersey-from-teamspyderphils-_mp4-0323_jpg.rf.2c3243f43e8fe1ce73fb7b2cf6e70dd0.jpg: 640x384 1 Cycling Helmet, 8.2ms
image 470/568 /content/Helmet-Detector-1/test/images/Quality-Affordable-Cycling-Helmet-Eyewear-Jersey-from-teamspyderphils-_mp4-0335_jpg.rf.136b2fe8b9612dd4878c9abb03fefea0.jpg: 640x384 1 Cycling Helmet, 7.8ms
image 471/568 /content/Helmet-Detector-1/test/images/Quality-Affordable-Cycling-Helmet-Eyewear-Jersey-from-teamspyderphils-_mp4-0337_jpg.rf.ac32b576e07ca259508445ac6f8e41eb.jpg: 640x384 1 Cycling Helmet, 7.6ms
image 472/568 /content/Helmet-Detector-1/test/images/USAPANG-NUTSHELL-BIKE-HELMETS-ABOUT-NUTSHELL-HELMETS-_mp4-0008_jpg.rf.1d3638ae4e79683fb5bd1fe814666b03.jpg: 384x640 5 nutshells, 8.3ms
image 473/568 /content/Helmet-Detector-1/test/images/USAPANG-NUTSHELL-BIKE-HELMETS-ABOUT-NUTSHELL-HELMETS-_mp4-0011_jpg.rf.f6dd74829c0c5fa208d7c9be8657240f.jpg: 384x640 5 nutshells, 7.7ms
image 474/568 /content/Helmet-Detector-1/test/images/USAPANG-NUTSHELL-BIKE-HELMETS-ABOUT-NUTSHELL-HELMETS-_mp4-0012_jpg.rf.5110cccdd755c8203816657e74ff50c0.jpg: 384x640 5 nutshells, 7.7ms
image 475/568 /content/Helmet-Detector-1/test/images/USAPANG-NUTSHELL-BIKE-HELMETS-ABOUT-NUTSHELL-HELMETS-_mp4-0013_jpg.rf.ece1b71520a7775288d4ddf15202ccbc.jpg: 384x640 5 nutshells, 7.6ms
image 476/568 /content/Helmet-Detector-1/test/images/USAPANG-NUTSHELL-BIKE-HELMETS-ABOUT-NUTSHELL-HELMETS-_mp4-0014_jpg.rf.ecc2e850a12544fb021dd32f6de89a48.jpg: 384x640 5 nutshells, 7.6ms
image 477/568 /content/Helmet-Detector-1/test/images/USAPANG-NUTSHELL-BIKE-HELMETS-ABOUT-NUTSHELL-HELMETS-_mp4-0022_jpg.rf.8250e3693b23249835e3e530ee4301d0.jpg: 384x640 5 nutshells, 7.6ms
image 478/568 /content/Helmet-Detector-1/test/images/USAPANG-NUTSHELL-BIKE-HELMETS-ABOUT-NUTSHELL-HELMETS-_mp4-0023_jpg.rf.ce91ef63171bf4a35e07aabbba2d9e08.jpg: 384x640 5 nutshells, 7.9ms
image 479/568 /content/Helmet-Detector-1/test/images/USAPANG-NUTSHELL-BIKE-HELMETS-ABOUT-NUTSHELL-HELMETS-_mp4-0025_jpg.rf.0725c9e2f52d3371f0aab9617996ee90.jpg: 384x640 5 nutshells, 7.8ms
image 480/568 /content/Helmet-Detector-1/test/images/USAPANG-NUTSHELL-BIKE-HELMETS-ABOUT-NUTSHELL-HELMETS-_mp4-0025_jpg.rf.e323a8a132cbc8e950f01f2473724fa6.jpg: 384x640 5 nutshells, 7.6ms
image 481/568 /content/Helmet-Detector-1/test/images/USAPANG-NUTSHELL-BIKE-HELMETS-ABOUT-NUTSHELL-HELMETS-_mp4-0026_jpg.rf.d881300f8bea6da747f122610e5bc223.jpg: 384x640 5 nutshells, 7.5ms
image 482/568 /content/Helmet-Detector-1/test/images/USAPANG-NUTSHELL-BIKE-HELMETS-ABOUT-NUTSHELL-HELMETS-_mp4-0032_jpg.rf.5d6fb19a234ecdd9d4ed8765cf10aff4.jpg: 384x640 5 nutshells, 7.7ms
image 483/568 /content/Helmet-Detector-1/test/images/USAPANG-NUTSHELL-BIKE-HELMETS-ABOUT-NUTSHELL-HELMETS-_mp4-0034_jpg.rf.e7fc1c75274737fecf61a970b2f76ea8.jpg: 384x640 5 nutshells, 7.7ms
image 484/568 /content/Helmet-Detector-1/test/images/USAPANG-NUTSHELL-BIKE-HELMETS-ABOUT-NUTSHELL-HELMETS-_mp4-0041_jpg.rf.c950c106dd05b0753fe5ba6e6674f161.jpg: 384x640 4 nutshells, 10.4ms
image 485/568 /content/Helmet-Detector-1/test/images/USAPANG-NUTSHELL-BIKE-HELMETS-ABOUT-NUTSHELL-HELMETS-_mp4-0043_jpg.rf.615933324836a0931b5243fb5a99c565.jpg: 384x640 4 nutshells, 8.2ms
image 486/568 /content/Helmet-Detector-1/test/images/USAPANG-NUTSHELL-BIKE-HELMETS-ABOUT-NUTSHELL-HELMETS-_mp4-0059_jpg.rf.c7cee3f05334bcb2d90120605f073a53.jpg: 384x640 1 nutshell, 7.9ms
image 487/568 /content/Helmet-Detector-1/test/images/USAPANG-NUTSHELL-BIKE-HELMETS-ABOUT-NUTSHELL-HELMETS-_mp4-0061_jpg.rf.84e9a50a7c25660620d5677652c1c847.jpg: 384x640 3 nutshells, 8.0ms
image 488/568 /content/Helmet-Detector-1/test/images/USAPANG-NUTSHELL-BIKE-HELMETS-ABOUT-NUTSHELL-HELMETS-_mp4-0065_jpg.rf.917eaac6c405c452f56bfb05d4208c9f.jpg: 384x640 2 nutshells, 8.0ms
image 489/568 /content/Helmet-Detector-1/test/images/USAPANG-NUTSHELL-BIKE-HELMETS-ABOUT-NUTSHELL-HELMETS-_mp4-0068_jpg.rf.5445abba45d5e2223c971a89753feb0e.jpg: 384x640 2 nutshells, 7.8ms
image 490/568 /content/Helmet-Detector-1/test/images/USAPANG-NUTSHELL-BIKE-HELMETS-ABOUT-NUTSHELL-HELMETS-_mp4-0070_jpg.rf.22c5e4cf27f98ad2904bc7851ff4f74b.jpg: 384x640 2 nutshells, 8.8ms
image 491/568 /content/Helmet-Detector-1/test/images/USAPANG-NUTSHELL-BIKE-HELMETS-ABOUT-NUTSHELL-HELMETS-_mp4-0074_jpg.rf.b121e37bbbb844d0f2fc47291fa4cb0e.jpg: 384x640 3 nutshells, 8.2ms
image 492/568 /content/Helmet-Detector-1/test/images/USAPANG-NUTSHELL-BIKE-HELMETS-ABOUT-NUTSHELL-HELMETS-_mp4-0077_jpg.rf.7ef1067a5a155d2ef7333479e0a4cf9c.jpg: 384x640 3 nutshells, 7.7ms
image 493/568 /content/Helmet-Detector-1/test/images/USAPANG-NUTSHELL-BIKE-HELMETS-ABOUT-NUTSHELL-HELMETS-_mp4-0080_jpg.rf.fb75ae1058d66ed576d5dc1cd4d9e0d9.jpg: 384x640 3 nutshells, 8.3ms
image 494/568 /content/Helmet-Detector-1/test/images/USAPANG-NUTSHELL-BIKE-HELMETS-ABOUT-NUTSHELL-HELMETS-_mp4-0604_jpg.rf.5fa78c3135a7aeb4d4c60b0e0785d1a1.jpg: 384x640 3 nutshells, 8.1ms
image 495/568 /content/Helmet-Detector-1/test/images/USAPANG-NUTSHELL-BIKE-HELMETS-ABOUT-NUTSHELL-HELMETS-_mp4-0656_jpg.rf.7b2a902915504d40f87451df31da7239.jpg: 384x640 3 nutshells, 8.6ms
image 496/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0014_jpg.rf.42cff63e1b8c47f423e29d89a6d3e8c8.jpg: 384x640 3 quarter face helmets, 8.2ms
image 497/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0016_jpg.rf.b09331e0b04cd75e57cfe75723155b4f.jpg: 384x640 3 quarter face helmets, 8.0ms
image 498/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0024_jpg.rf.3c2ccb37593ed2252ca9e8482187d6e7.jpg: 384x640 3 quarter face helmets, 9.9ms
image 499/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0037_jpg.rf.a61f1efc6ae8c9f6c8de80b32c867327.jpg: 384x640 3 quarter face helmets, 8.0ms
image 500/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0039_jpg.rf.733c26756676cdd10b8e9e8290678255.jpg: 384x640 3 quarter face helmets, 7.9ms
image 501/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0045_jpg.rf.b427891b07557a182f10addbcae1cc92.jpg: 384x640 3 quarter face helmets, 7.8ms
image 502/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0054_jpg.rf.6a95ca56ab5334d64b3596eba757a62a.jpg: 384x640 3 quarter face helmets, 8.4ms
image 503/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0061_jpg.rf.9ad084271fab15158461e3cfa1615138.jpg: 384x640 3 quarter face helmets, 7.7ms
image 504/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0064_jpg.rf.2ddfd6f1bb02b703fef104537656c2ac.jpg: 384x640 3 quarter face helmets, 8.0ms
image 505/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0067_jpg.rf.345a983c46e80d31dd9e3596d06dfd2d.jpg: 384x640 3 quarter face helmets, 8.0ms
image 506/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0076_jpg.rf.d379af0d284db7de46f495a96638654a.jpg: 384x640 1 quarter face helmet, 10.4ms
image 507/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0081_jpg.rf.1e846f550a3abbb9a2412e85bf6792d6.jpg: 384x640 1 quarter face helmet, 8.3ms
image 508/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0090_jpg.rf.9c858fcbd2a963d862b791d42fa04de4.jpg: 384x640 1 quarter face helmet, 8.1ms
image 509/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0091_jpg.rf.7934cf31f9f2241dc6004fdadb87bca5.jpg: 384x640 1 quarter face helmet, 8.0ms
image 510/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0096_jpg.rf.89b0573f0197bc883e61a158b3899ec5.jpg: 384x640 1 quarter face helmet, 8.8ms
image 511/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0098_jpg.rf.0596f2cbce22929662e04bce8c96f8fa.jpg: 384x640 1 quarter face helmet, 8.3ms
image 512/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0151_jpg.rf.c78d0b68586cdd7f92cb18c00aeb7b23.jpg: 384x640 3 quarter face helmets, 15.4ms
image 513/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0154_jpg.rf.66dea5e069b4a0a2c9643ba255685984.jpg: 384x640 3 quarter face helmets, 10.8ms
image 514/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0163_jpg.rf.1a7fdcc91b0c7b00720e3f265e4c14ca.jpg: 384x640 3 quarter face helmets, 8.7ms
image 515/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0168_jpg.rf.b162f8cf290b727aead7f3721aa514ee.jpg: 384x640 3 quarter face helmets, 9.1ms
image 516/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0172_jpg.rf.179b67137fe412284a81073ce3330371.jpg: 384x640 3 quarter face helmets, 8.2ms
image 517/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0173_jpg.rf.f1c79444b1a2853e50e5d7662b377379.jpg: 384x640 3 quarter face helmets, 8.9ms
image 518/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0192_jpg.rf.32c4988168a7bd9fff368d305f6a924d.jpg: 384x640 3 quarter face helmets, 8.1ms
image 519/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0198_jpg.rf.c00085ea336b1e43db7931501a497330.jpg: 384x640 3 quarter face helmets, 11.3ms
image 520/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0208_jpg.rf.6ae1269fa9640bcb791c6650c8d9d6f4.jpg: 384x640 3 quarter face helmets, 8.6ms
image 521/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0209_jpg.rf.69523e50b2d4fc05fc509d33ea05bc5b.jpg: 384x640 3 quarter face helmets, 8.6ms
image 522/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0217_jpg.rf.7d70bdaab4f4b6867dd2f75c80c2743b.jpg: 384x640 1 quarter face helmet, 8.1ms
image 523/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0221_jpg.rf.8cbe8ed59331fd8da83f4dc2c4d46901.jpg: 384x640 1 quarter face helmet, 8.5ms
image 524/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0222_jpg.rf.4924bedea44e1c052012c9689138e084.jpg: 384x640 1 quarter face helmet, 8.1ms
image 525/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0234_jpg.rf.9ca2a83f5cc9f87bedd9cd68b97684fc.jpg: 384x640 1 quarter face helmet, 8.4ms
image 526/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0259_jpg.rf.99a5bc4e9a719b6f91618908f83fad9a.jpg: 384x640 3 quarter face helmets, 8.4ms
image 527/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0267_jpg.rf.2d1fe1616ce3f7cd8ad55d6c9f7a8599.jpg: 384x640 3 quarter face helmets, 8.6ms
image 528/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0271_jpg.rf.396046d7839983de886b7a5ed2deec4f.jpg: 384x640 3 quarter face helmets, 8.7ms
image 529/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0273_jpg.rf.7d844876644351e119ede2e6de94e21d.jpg: 384x640 3 quarter face helmets, 10.4ms
image 530/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0281_jpg.rf.2181bdbaa0c33200e1f703ec3adf583a.jpg: 384x640 3 quarter face helmets, 14.0ms
image 531/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0289_jpg.rf.d485414df1433378ac873fa381314388.jpg: 384x640 2 quarter face helmets, 8.3ms
image 532/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0290_jpg.rf.0eebb0f4c3f70558307e4966695869bf.jpg: 384x640 2 quarter face helmets, 8.6ms
image 533/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0297_jpg.rf.10d5cd45e46ee7febc39756423cb5302.jpg: 384x640 2 quarter face helmets, 8.6ms
image 534/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0301_jpg.rf.f71cf41122efc2c8d52c06fd3f49ffbe.jpg: 384x640 2 quarter face helmets, 9.6ms
image 535/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0304_jpg.rf.6355d0448300a8123e609e0c1be3eb2f.jpg: 384x640 2 quarter face helmets, 8.1ms
image 536/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0310_jpg.rf.831ae8e14976130205c55f59875a7ba6.jpg: 384x640 3 quarter face helmets, 11.4ms
image 537/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0323_jpg.rf.9e82caf876816018a821e8ca23020f03.jpg: 384x640 2 quarter face helmets, 8.3ms
image 538/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0335_jpg.rf.54dbb953523ef4d3887e4e83fcc1f6df.jpg: 384x640 3 quarter face helmets, 11.2ms
image 539/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0336_jpg.rf.9958a3375c1e74b67ff7e490fbacfd1a.jpg: 384x640 3 quarter face helmets, 8.1ms
image 540/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0338_jpg.rf.9f32eefa7770127436839ff57fd4c3a2.jpg: 384x640 2 quarter face helmets, 8.5ms
image 541/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0346_jpg.rf.e7d6b0973f08d05755a36a2d42f21a6e.jpg: 384x640 2 quarter face helmets, 8.1ms
image 542/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0351_jpg.rf.bd8ae64af977d1a14f6c23b89b58715e.jpg: 384x640 2 quarter face helmets, 8.2ms
image 543/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0357_jpg.rf.74c69099b1f3710e99555bb7a039a7b8.jpg: 384x640 2 quarter face helmets, 8.2ms
image 544/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0359_jpg.rf.134c69b65221ff0c01d9574bca5aadea.jpg: 384x640 2 quarter face helmets, 8.2ms
image 545/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0367_jpg.rf.838ad5260639258617eb59080c095f02.jpg: 384x640 2 quarter face helmets, 8.6ms
image 546/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0369_jpg.rf.d488ff659df49c1781d66ef1fb4614b5.jpg: 384x640 2 quarter face helmets, 8.4ms
image 547/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0372_jpg.rf.2d89d4cb51d6baf1f9418a32e6f2da99.jpg: 384x640 3 quarter face helmets, 8.2ms
image 548/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0475_jpg.rf.beaa5a3972011ca01980889f4d280121.jpg: 384x640 2 quarter face helmets, 8.3ms
image 549/568 /content/Helmet-Detector-1/test/images/Vega-Standard-3_4-Helmet_mp4-0490_jpg.rf.4ef00336af9ef26f1b414c09d83d3616.jpg: 384x640 2 quarter face helmets, 8.0ms
image 550/568 /content/Helmet-Detector-1/test/images/What-full-face-helmet-do-you-prefer__mp4-0040_jpg.rf.f3434b7b52c08c78127be04d5427d7be.jpg: 640x384 1 sports helmet, 8.8ms
image 551/568 /content/Helmet-Detector-1/test/images/What-full-face-helmet-do-you-prefer__mp4-0047_jpg.rf.d49d89f5a494afad0a0dea3eb7ddaf69.jpg: 640x384 1 sports helmet, 8.2ms
image 552/568 /content/Helmet-Detector-1/test/images/What-full-face-helmet-do-you-prefer__mp4-0050_jpg.rf.14b91e5b129171af073e190ff6593d89.jpg: 640x384 1 sports helmet, 8.5ms
image 553/568 /content/Helmet-Detector-1/test/images/What-full-face-helmet-do-you-prefer__mp4-0077_jpg.rf.040980a7499c9ceb99471f1df73aaab1.jpg: 640x384 1 sports helmet, 8.3ms
image 554/568 /content/Helmet-Detector-1/test/images/What-full-face-helmet-do-you-prefer__mp4-0089_jpg.rf.9b059c948d74384901bf97213dad10a9.jpg: 640x384 1 sports helmet, 8.2ms
image 555/568 /content/Helmet-Detector-1/test/images/What-full-face-helmet-do-you-prefer__mp4-0091_jpg.rf.f6e9f28d91c967e1ac839043aeeab702.jpg: 640x384 1 sports helmet, 8.2ms
image 556/568 /content/Helmet-Detector-1/test/images/photo1704804010-5-_jpeg.rf.f486544bc420f5cbc2b213e7647f9202.jpg: 480x640 2 helmets, 43.0ms
image 557/568 /content/Helmet-Detector-1/test/images/photo1704804020-3-_jpeg.rf.1ccf88731691506843112a3dc51ba367.jpg: 640x480 1 helmet, 10.0ms
image 558/568 /content/Helmet-Detector-1/test/images/photo1704804020-6-_jpeg.rf.40ac7a3ab9f504d33e6853396622e6f0.jpg: 640x480 1 helmet, 8.6ms
image 559/568 /content/Helmet-Detector-1/test/images/photo1704804020-7-_jpeg.rf.17b2011c0782984ad0814e8cc5fc0191.jpg: 640x480 2 helmets, 8.4ms
image 560/568 /content/Helmet-Detector-1/test/images/photo1704804020-8-_jpeg.rf.fbe99a2aaa4a7b359b6a5b70884f0f33.jpg: 640x480 1 helmet, 8.8ms
image 561/568 /content/Helmet-Detector-1/test/images/photo1704804020_jpeg.rf.be3fa7642e67a0dcdd7588e60fdfb6ea.jpg: 640x480 1 helmet, 8.9ms
image 562/568 /content/Helmet-Detector-1/test/images/photo1704804033-1-_jpeg.rf.36e48d76feeef95dcde96814143b1c11.jpg: 640x480 1 helmet, 8.4ms
image 563/568 /content/Helmet-Detector-1/test/images/photo1704804033-7-_jpeg.rf.c968fbce5f07a00f95a88eb6810d393a.jpg: 640x480 1 helmet, 8.1ms
image 564/568 /content/Helmet-Detector-1/test/images/photo1704804033-8-_jpeg.rf.07534712da4f7eca542f268ef7b4c4c1.jpg: 640x480 1 helmet, 8.6ms
image 565/568 /content/Helmet-Detector-1/test/images/photo1704804041_jpeg.rf.846a9ca2ea3f2c27dfc8c34444a53475.jpg: 640x480 1 helmet, 8.4ms
image 566/568 /content/Helmet-Detector-1/test/images/photo1704804048-6-_jpeg.rf.aec88f87f470e466fe66a47b314555b9.jpg: 640x480 1 helmet, 8.5ms
image 567/568 /content/Helmet-Detector-1/test/images/photo1704804048-8-_jpeg.rf.140a4dea84b1935f5be39eabe796feaf.jpg: 640x480 1 helmet, 10.8ms
image 568/568 /content/Helmet-Detector-1/test/images/photo1704804050_jpeg.rf.cb48f7355507b1ee249c9ab23d0ca0f7.jpg: 640x480 1 helmet, 12.6ms
Speed: 1.4ms preprocess, 9.7ms inference, 2.3ms postprocess per image at shape (1, 3, 640, 480)
Results saved to runs/detect/predict
💡 Learn more at https://docs.ultralytics.com/modes/predict

import glob
import os
from IPython.display import Image as IPyImage, display

latest_folder = max(glob.glob('/content/runs/detect/predict*/'), key=os.path.getmtime)
for img in glob.glob(f'{latest_folder}/*.jpg')[1:4]:
    display(IPyImage(filename=img, width=600))
    print("\n")
     







!yolo task=detect mode=predict model= "/content/runs/detect/train/weights/best.pt" conf=0.25 source=helmet.jpg save=True
     
Ultralytics 8.3.17 🚀 Python-3.10.12 torch-2.4.1+cu121 CUDA:0 (Tesla T4, 15102MiB)
YOLO11n summary (fused): 238 layers, 2,584,687 parameters, 0 gradients, 6.3 GFLOPs

image 1/1 /content/helmet.jpg: 640x384 1 nutshell, 77.5ms
Speed: 3.5ms preprocess, 77.5ms inference, 1046.6ms postprocess per image at shape (1, 3, 640, 384)
Results saved to runs/detect/predict2
💡 Learn more at https://docs.ultralytics.com/modes/predict

Image("/content/runs/detect/predict2/helmet.jpg", width=600)
     

Step # 08 Inference with Custom Model on Videos


!yolo task=detect mode=predict model= "/content/runs/detect/train/weights/best.pt" conf=0.25 source="PPE_Part1.mp4" save=True
     
Ultralytics 8.3.3 🚀 Python-3.10.12 torch-2.4.1+cu121 CUDA:0 (Tesla T4, 15102MiB)
YOLO11n summary (fused): 238 layers, 2,583,517 parameters, 0 gradients, 6.3 GFLOPs

video 1/1 (frame 1/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 1 Protective Helmet, 48.5ms
video 1/1 (frame 2/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 2 Protective Helmets, 12.5ms
video 1/1 (frame 3/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 2 Protective Helmets, 9.5ms
video 1/1 (frame 4/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 2 Protective Helmets, 9.2ms
video 1/1 (frame 5/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 2 Protective Helmets, 9.9ms
video 1/1 (frame 6/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 2 Protective Helmets, 9.6ms
video 1/1 (frame 7/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 3 Protective Helmets, 8.8ms
video 1/1 (frame 8/310) /content/PPE_Part1.mp4: 384x640 2 Jackets, 2 Protective Helmets, 9.3ms
video 1/1 (frame 9/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 2 Protective Helmets, 9.0ms
video 1/1 (frame 10/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 2 Protective Helmets, 12.2ms
video 1/1 (frame 11/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 3 Protective Helmets, 9.0ms
video 1/1 (frame 12/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 3 Protective Helmets, 9.4ms
video 1/1 (frame 13/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 4 Protective Helmets, 8.9ms
video 1/1 (frame 14/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 3 Protective Helmets, 9.1ms
video 1/1 (frame 15/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 3 Protective Helmets, 8.9ms
video 1/1 (frame 16/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 3 Protective Helmets, 9.0ms
video 1/1 (frame 17/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 3 Protective Helmets, 9.1ms
video 1/1 (frame 18/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 3 Protective Helmets, 12.5ms
video 1/1 (frame 19/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 3 Protective Helmets, 9.4ms
video 1/1 (frame 20/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 1 Protective Boots, 3 Protective Helmets, 8.8ms
video 1/1 (frame 21/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 1 Protective Boots, 3 Protective Helmets, 9.1ms
video 1/1 (frame 22/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 1 Protective Boots, 3 Protective Helmets, 9.1ms
video 1/1 (frame 23/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 1 Protective Boots, 3 Protective Helmets, 9.0ms
video 1/1 (frame 24/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.0ms
video 1/1 (frame 25/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 1 Protective Boots, 3 Protective Helmets, 9.2ms
video 1/1 (frame 26/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 1 Protective Boots, 3 Protective Helmets, 12.5ms
video 1/1 (frame 27/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 1 Protective Boots, 3 Protective Helmets, 9.9ms
video 1/1 (frame 28/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 1 Protective Boots, 3 Protective Helmets, 9.2ms
video 1/1 (frame 29/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 1 Protective Boots, 3 Protective Helmets, 9.4ms
video 1/1 (frame 30/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 2 Protective Bootss, 2 Protective Helmets, 9.2ms
video 1/1 (frame 31/310) /content/PPE_Part1.mp4: 384x640 7 Jackets, 3 Protective Bootss, 2 Protective Helmets, 9.4ms
video 1/1 (frame 32/310) /content/PPE_Part1.mp4: 384x640 8 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.4ms
video 1/1 (frame 33/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 1 Protective Boots, 3 Protective Helmets, 9.1ms
video 1/1 (frame 34/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 1 Protective Boots, 3 Protective Helmets, 12.7ms
video 1/1 (frame 35/310) /content/PPE_Part1.mp4: 384x640 7 Jackets, 2 Protective Bootss, 3 Protective Helmets, 10.0ms
video 1/1 (frame 36/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 2 Protective Bootss, 2 Protective Helmets, 9.6ms
video 1/1 (frame 37/310) /content/PPE_Part1.mp4: 384x640 7 Jackets, 2 Protective Bootss, 2 Protective Helmets, 9.5ms
video 1/1 (frame 38/310) /content/PPE_Part1.mp4: 384x640 8 Jackets, 1 Protective Boots, 3 Protective Helmets, 9.8ms
video 1/1 (frame 39/310) /content/PPE_Part1.mp4: 384x640 7 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.6ms
video 1/1 (frame 40/310) /content/PPE_Part1.mp4: 384x640 7 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.0ms
video 1/1 (frame 41/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.4ms
video 1/1 (frame 42/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 3 Protective Bootss, 3 Protective Helmets, 12.9ms
video 1/1 (frame 43/310) /content/PPE_Part1.mp4: 384x640 7 Jackets, 2 Protective Bootss, 3 Protective Helmets, 10.1ms
video 1/1 (frame 44/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 3 Protective Bootss, 3 Protective Helmets, 9.2ms
video 1/1 (frame 45/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.3ms
video 1/1 (frame 46/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.1ms
video 1/1 (frame 47/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 3 Protective Bootss, 3 Protective Helmets, 9.0ms
video 1/1 (frame 48/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 4 Protective Bootss, 3 Protective Helmets, 9.3ms
video 1/1 (frame 49/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 3 Protective Bootss, 3 Protective Helmets, 9.0ms
video 1/1 (frame 50/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.3ms
video 1/1 (frame 51/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.1ms
video 1/1 (frame 52/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 2 Protective Bootss, 3 Protective Helmets, 8.9ms
video 1/1 (frame 53/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 2 Protective Bootss, 3 Protective Helmets, 15.0ms
video 1/1 (frame 54/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 3 Protective Bootss, 3 Protective Helmets, 10.5ms
video 1/1 (frame 55/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 4 Protective Bootss, 4 Protective Helmets, 10.1ms
video 1/1 (frame 56/310) /content/PPE_Part1.mp4: 384x640 7 Jackets, 3 Protective Bootss, 3 Protective Helmets, 10.2ms
video 1/1 (frame 57/310) /content/PPE_Part1.mp4: 384x640 7 Jackets, 1 Protective Boots, 3 Protective Helmets, 9.9ms
video 1/1 (frame 58/310) /content/PPE_Part1.mp4: 384x640 7 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.9ms
video 1/1 (frame 59/310) /content/PPE_Part1.mp4: 384x640 7 Jackets, 3 Protective Bootss, 3 Protective Helmets, 9.4ms
video 1/1 (frame 60/310) /content/PPE_Part1.mp4: 384x640 7 Jackets, 3 Protective Bootss, 3 Protective Helmets, 10.1ms
video 1/1 (frame 61/310) /content/PPE_Part1.mp4: 384x640 8 Jackets, 3 Protective Bootss, 3 Protective Helmets, 12.9ms
video 1/1 (frame 62/310) /content/PPE_Part1.mp4: 384x640 8 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.8ms
video 1/1 (frame 63/310) /content/PPE_Part1.mp4: 384x640 9 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.3ms
video 1/1 (frame 64/310) /content/PPE_Part1.mp4: 384x640 9 Jackets, 2 Protective Bootss, 3 Protective Helmets, 10.1ms
video 1/1 (frame 65/310) /content/PPE_Part1.mp4: 384x640 8 Jackets, 2 Protective Bootss, 3 Protective Helmets, 10.3ms
video 1/1 (frame 66/310) /content/PPE_Part1.mp4: 384x640 8 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.5ms
video 1/1 (frame 67/310) /content/PPE_Part1.mp4: 384x640 8 Jackets, 2 Protective Bootss, 4 Protective Helmets, 10.4ms
video 1/1 (frame 68/310) /content/PPE_Part1.mp4: 384x640 7 Jackets, 3 Protective Bootss, 4 Protective Helmets, 10.1ms
video 1/1 (frame 69/310) /content/PPE_Part1.mp4: 384x640 7 Jackets, 2 Protective Bootss, 3 Protective Helmets, 11.1ms
video 1/1 (frame 70/310) /content/PPE_Part1.mp4: 384x640 7 Jackets, 2 Protective Bootss, 3 Protective Helmets, 10.0ms
video 1/1 (frame 71/310) /content/PPE_Part1.mp4: 384x640 7 Jackets, 3 Protective Bootss, 3 Protective Helmets, 10.2ms
video 1/1 (frame 72/310) /content/PPE_Part1.mp4: 384x640 8 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.7ms
video 1/1 (frame 73/310) /content/PPE_Part1.mp4: 384x640 9 Jackets, 2 Protective Bootss, 2 Protective Helmets, 9.3ms
video 1/1 (frame 74/310) /content/PPE_Part1.mp4: 384x640 9 Jackets, 3 Protective Bootss, 2 Protective Helmets, 9.9ms
video 1/1 (frame 75/310) /content/PPE_Part1.mp4: 384x640 8 Jackets, 6 Protective Bootss, 2 Protective Helmets, 10.0ms
video 1/1 (frame 76/310) /content/PPE_Part1.mp4: 384x640 8 Jackets, 6 Protective Bootss, 2 Protective Helmets, 10.2ms
video 1/1 (frame 77/310) /content/PPE_Part1.mp4: 384x640 8 Jackets, 3 Protective Bootss, 3 Protective Helmets, 14.6ms
video 1/1 (frame 78/310) /content/PPE_Part1.mp4: 384x640 8 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.2ms
video 1/1 (frame 79/310) /content/PPE_Part1.mp4: 384x640 8 Jackets, 3 Protective Bootss, 3 Protective Helmets, 10.5ms
video 1/1 (frame 80/310) /content/PPE_Part1.mp4: 384x640 8 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.0ms
video 1/1 (frame 81/310) /content/PPE_Part1.mp4: 384x640 8 Jackets, 2 Protective Bootss, 3 Protective Helmets, 10.8ms
video 1/1 (frame 82/310) /content/PPE_Part1.mp4: 384x640 8 Jackets, 2 Protective Bootss, 3 Protective Helmets, 10.0ms
video 1/1 (frame 83/310) /content/PPE_Part1.mp4: 384x640 8 Jackets, 3 Protective Bootss, 3 Protective Helmets, 10.2ms
video 1/1 (frame 84/310) /content/PPE_Part1.mp4: 384x640 8 Jackets, 3 Protective Bootss, 3 Protective Helmets, 9.1ms
video 1/1 (frame 85/310) /content/PPE_Part1.mp4: 384x640 8 Jackets, 4 Protective Bootss, 3 Protective Helmets, 16.3ms
video 1/1 (frame 86/310) /content/PPE_Part1.mp4: 384x640 8 Jackets, 7 Protective Bootss, 3 Protective Helmets, 14.8ms
video 1/1 (frame 87/310) /content/PPE_Part1.mp4: 384x640 7 Jackets, 2 Protective Bootss, 3 Protective Helmets, 16.9ms
video 1/1 (frame 88/310) /content/PPE_Part1.mp4: 384x640 8 Jackets, 3 Protective Bootss, 3 Protective Helmets, 9.8ms
video 1/1 (frame 89/310) /content/PPE_Part1.mp4: 384x640 7 Jackets, 3 Protective Bootss, 3 Protective Helmets, 9.8ms
video 1/1 (frame 90/310) /content/PPE_Part1.mp4: 384x640 7 Jackets, 3 Protective Bootss, 3 Protective Helmets, 9.7ms
video 1/1 (frame 91/310) /content/PPE_Part1.mp4: 384x640 7 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.2ms
video 1/1 (frame 92/310) /content/PPE_Part1.mp4: 384x640 8 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.2ms
video 1/1 (frame 93/310) /content/PPE_Part1.mp4: 384x640 8 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.2ms
video 1/1 (frame 94/310) /content/PPE_Part1.mp4: 384x640 8 Jackets, 2 Protective Bootss, 3 Protective Helmets, 8.5ms
video 1/1 (frame 95/310) /content/PPE_Part1.mp4: 384x640 8 Jackets, 3 Protective Bootss, 3 Protective Helmets, 9.8ms
video 1/1 (frame 96/310) /content/PPE_Part1.mp4: 384x640 8 Jackets, 4 Protective Bootss, 3 Protective Helmets, 9.3ms
video 1/1 (frame 97/310) /content/PPE_Part1.mp4: 384x640 9 Jackets, 2 Protective Bootss, 3 Protective Helmets, 8.7ms
video 1/1 (frame 98/310) /content/PPE_Part1.mp4: 384x640 8 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.8ms
video 1/1 (frame 99/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 1 Protective Boots, 3 Protective Helmets, 9.6ms
video 1/1 (frame 100/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 1 Protective Boots, 3 Protective Helmets, 9.7ms
video 1/1 (frame 101/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 3 Protective Bootss, 3 Protective Helmets, 14.4ms
video 1/1 (frame 102/310) /content/PPE_Part1.mp4: 384x640 8 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.6ms
video 1/1 (frame 103/310) /content/PPE_Part1.mp4: 384x640 7 Jackets, 3 Protective Bootss, 3 Protective Helmets, 9.8ms
video 1/1 (frame 104/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.8ms
video 1/1 (frame 105/310) /content/PPE_Part1.mp4: 384x640 7 Jackets, 1 Protective Boots, 3 Protective Helmets, 9.4ms
video 1/1 (frame 106/310) /content/PPE_Part1.mp4: 384x640 7 Jackets, 1 Protective Boots, 3 Protective Helmets, 9.6ms
video 1/1 (frame 107/310) /content/PPE_Part1.mp4: 384x640 8 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.8ms
video 1/1 (frame 108/310) /content/PPE_Part1.mp4: 384x640 7 Jackets, 3 Protective Bootss, 3 Protective Helmets, 9.7ms
video 1/1 (frame 109/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 3 Protective Bootss, 3 Protective Helmets, 14.2ms
video 1/1 (frame 110/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.2ms
video 1/1 (frame 111/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.0ms
video 1/1 (frame 112/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.7ms
video 1/1 (frame 113/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 3 Protective Bootss, 2 Protective Helmets, 10.3ms
video 1/1 (frame 114/310) /content/PPE_Part1.mp4: 384x640 7 Jackets, 3 Protective Bootss, 2 Protective Helmets, 9.2ms
video 1/1 (frame 115/310) /content/PPE_Part1.mp4: 384x640 7 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.3ms
video 1/1 (frame 116/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 3 Protective Helmets, 10.1ms
video 1/1 (frame 117/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 1 Protective Boots, 3 Protective Helmets, 9.9ms
video 1/1 (frame 118/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 1 Protective Boots, 3 Protective Helmets, 10.1ms
video 1/1 (frame 119/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Helmets, 9.9ms
video 1/1 (frame 120/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 2 Protective Bootss, 3 Protective Helmets, 10.0ms
video 1/1 (frame 121/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 1 Protective Boots, 3 Protective Helmets, 10.1ms
video 1/1 (frame 122/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Helmets, 10.0ms
video 1/1 (frame 123/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 1 Protective Boots, 3 Protective Helmets, 9.9ms
video 1/1 (frame 124/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 1 Protective Boots, 3 Protective Helmets, 10.2ms
video 1/1 (frame 125/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 3 Protective Helmets, 15.0ms
video 1/1 (frame 126/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 1 Protective Boots, 3 Protective Helmets, 9.8ms
video 1/1 (frame 127/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 1 Protective Boots, 4 Protective Helmets, 9.6ms
video 1/1 (frame 128/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 1 Protective Boots, 3 Protective Helmets, 9.2ms
video 1/1 (frame 129/310) /content/PPE_Part1.mp4: 384x640 7 Jackets, 1 Protective Boots, 3 Protective Helmets, 9.2ms
video 1/1 (frame 130/310) /content/PPE_Part1.mp4: 384x640 7 Jackets, 1 Protective Boots, 3 Protective Helmets, 9.2ms
video 1/1 (frame 131/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.4ms
video 1/1 (frame 132/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.1ms
video 1/1 (frame 133/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 3 Protective Helmets, 13.5ms
video 1/1 (frame 134/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 2 Protective Helmets, 9.1ms
video 1/1 (frame 135/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 2 Protective Helmets, 9.0ms
video 1/1 (frame 136/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 2 Protective Helmets, 9.1ms
video 1/1 (frame 137/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 2 Protective Helmets, 9.2ms
video 1/1 (frame 138/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 3 Protective Helmets, 9.0ms
video 1/1 (frame 139/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 1 Protective Boots, 3 Protective Helmets, 9.1ms
video 1/1 (frame 140/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.0ms
video 1/1 (frame 141/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.5ms
video 1/1 (frame 142/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.0ms
video 1/1 (frame 143/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 3 Protective Bootss, 3 Protective Helmets, 9.5ms
video 1/1 (frame 144/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 4 Protective Bootss, 2 Protective Helmets, 9.3ms
video 1/1 (frame 145/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Bootss, 2 Protective Helmets, 10.2ms
video 1/1 (frame 146/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Bootss, 3 Protective Helmets, 10.5ms
video 1/1 (frame 147/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Bootss, 3 Protective Helmets, 9.3ms
video 1/1 (frame 148/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Bootss, 3 Protective Helmets, 9.6ms
video 1/1 (frame 149/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 3 Protective Bootss, 3 Protective Helmets, 14.1ms
video 1/1 (frame 150/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 2 Protective Bootss, 3 Protective Helmets, 10.3ms
video 1/1 (frame 151/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 3 Protective Bootss, 3 Protective Helmets, 9.5ms
video 1/1 (frame 152/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 1 Protective Boots, 3 Protective Helmets, 9.2ms
video 1/1 (frame 153/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 1 Protective Boots, 3 Protective Helmets, 9.7ms
video 1/1 (frame 154/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 1 Protective Boots, 3 Protective Helmets, 9.3ms
video 1/1 (frame 155/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 1 Protective Boots, 3 Protective Helmets, 9.8ms
video 1/1 (frame 156/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 3 Protective Helmets, 9.4ms
video 1/1 (frame 157/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 1 Protective Boots, 3 Protective Helmets, 13.8ms
video 1/1 (frame 158/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.4ms
video 1/1 (frame 159/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 4 Protective Bootss, 3 Protective Helmets, 9.3ms
video 1/1 (frame 160/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 4 Protective Bootss, 3 Protective Helmets, 9.3ms
video 1/1 (frame 161/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 3 Protective Bootss, 3 Protective Helmets, 10.7ms
video 1/1 (frame 162/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 3 Protective Bootss, 3 Protective Helmets, 9.5ms
video 1/1 (frame 163/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 3 Protective Bootss, 3 Protective Helmets, 9.8ms
video 1/1 (frame 164/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.9ms
video 1/1 (frame 165/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Bootss, 3 Protective Helmets, 9.6ms
video 1/1 (frame 166/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.5ms
video 1/1 (frame 167/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 3 Protective Bootss, 3 Protective Helmets, 10.0ms
video 1/1 (frame 168/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 3 Protective Bootss, 3 Protective Helmets, 10.3ms
video 1/1 (frame 169/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 3 Protective Bootss, 3 Protective Helmets, 10.6ms
video 1/1 (frame 170/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 3 Protective Bootss, 3 Protective Helmets, 9.5ms
video 1/1 (frame 171/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 3 Protective Bootss, 3 Protective Helmets, 12.0ms
video 1/1 (frame 172/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 3 Protective Bootss, 3 Protective Helmets, 13.3ms
video 1/1 (frame 173/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 2 Protective Bootss, 3 Protective Helmets, 13.9ms
video 1/1 (frame 174/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 3 Protective Bootss, 3 Protective Helmets, 9.2ms
video 1/1 (frame 175/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 3 Protective Bootss, 3 Protective Helmets, 9.1ms
video 1/1 (frame 176/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 3 Protective Bootss, 3 Protective Helmets, 9.2ms
video 1/1 (frame 177/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 1 Protective Boots, 3 Protective Helmets, 9.2ms
video 1/1 (frame 178/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 1 Protective Boots, 3 Protective Helmets, 9.3ms
video 1/1 (frame 179/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.4ms
video 1/1 (frame 180/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 2 Protective Bootss, 3 Protective Helmets, 13.7ms
video 1/1 (frame 181/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 4 Protective Bootss, 3 Protective Helmets, 13.7ms
video 1/1 (frame 182/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Bootss, 3 Protective Helmets, 9.2ms
video 1/1 (frame 183/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Bootss, 2 Protective Helmets, 9.4ms
video 1/1 (frame 184/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Bootss, 2 Protective Helmets, 9.2ms
video 1/1 (frame 185/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 2 Protective Bootss, 2 Protective Helmets, 13.4ms
video 1/1 (frame 186/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Bootss, 2 Protective Helmets, 9.4ms
video 1/1 (frame 187/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Bootss, 3 Protective Helmets, 9.2ms
video 1/1 (frame 188/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 2 Protective Bootss, 3 Protective Helmets, 13.4ms
video 1/1 (frame 189/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 1 Protective Boots, 3 Protective Helmets, 9.6ms
video 1/1 (frame 190/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 1 Protective Boots, 3 Protective Helmets, 9.3ms
video 1/1 (frame 191/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Bootss, 3 Protective Helmets, 9.2ms
video 1/1 (frame 192/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Bootss, 3 Protective Helmets, 9.9ms
video 1/1 (frame 193/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 5 Protective Bootss, 2 Protective Helmets, 14.7ms
video 1/1 (frame 194/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Bootss, 2 Protective Helmets, 9.9ms
video 1/1 (frame 195/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Bootss, 3 Protective Helmets, 9.8ms
video 1/1 (frame 196/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Bootss, 2 Protective Helmets, 14.2ms
video 1/1 (frame 197/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Bootss, 3 Protective Helmets, 9.8ms
video 1/1 (frame 198/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 4 Protective Bootss, 3 Protective Helmets, 9.7ms
video 1/1 (frame 199/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Bootss, 1 Protective Helmet, 9.3ms
video 1/1 (frame 200/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 2 Protective Bootss, 2 Protective Helmets, 9.3ms
video 1/1 (frame 201/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 2 Protective Bootss, 3 Protective Helmets, 8.8ms
video 1/1 (frame 202/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.3ms
video 1/1 (frame 203/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.2ms
video 1/1 (frame 204/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Bootss, 3 Protective Helmets, 9.2ms
video 1/1 (frame 205/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 4 Protective Bootss, 3 Protective Helmets, 9.4ms
video 1/1 (frame 206/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Bootss, 3 Protective Helmets, 9.0ms
video 1/1 (frame 207/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 4 Protective Bootss, 2 Protective Helmets, 9.1ms
video 1/1 (frame 208/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 4 Protective Bootss, 2 Protective Helmets, 9.0ms
video 1/1 (frame 209/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 2 Protective Bootss, 2 Protective Helmets, 9.4ms
video 1/1 (frame 210/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.1ms
video 1/1 (frame 211/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Bootss, 3 Protective Helmets, 9.0ms
video 1/1 (frame 212/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 4 Protective Bootss, 3 Protective Helmets, 9.1ms
video 1/1 (frame 213/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Bootss, 3 Protective Helmets, 9.0ms
video 1/1 (frame 214/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Bootss, 3 Protective Helmets, 9.0ms
video 1/1 (frame 215/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 4 Protective Bootss, 3 Protective Helmets, 9.4ms
video 1/1 (frame 216/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 2 Protective Bootss, 3 Protective Helmets, 8.8ms
video 1/1 (frame 217/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 2 Protective Bootss, 2 Protective Helmets, 10.4ms
video 1/1 (frame 218/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 1 Protective Boots, 2 Protective Helmets, 8.9ms
video 1/1 (frame 219/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.1ms
video 1/1 (frame 220/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 2 Protective Bootss, 3 Protective Helmets, 8.9ms
video 1/1 (frame 221/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 1 Protective Boots, 3 Protective Helmets, 9.1ms
video 1/1 (frame 222/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 4 Protective Helmets, 8.8ms
video 1/1 (frame 223/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 1 Protective Boots, 4 Protective Helmets, 9.0ms
video 1/1 (frame 224/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 2 Protective Bootss, 4 Protective Helmets, 8.8ms
video 1/1 (frame 225/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.4ms
video 1/1 (frame 226/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 2 Protective Bootss, 3 Protective Helmets, 8.9ms
video 1/1 (frame 227/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Bootss, 4 Protective Helmets, 9.8ms
video 1/1 (frame 228/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 1 Protective Boots, 4 Protective Helmets, 9.2ms
video 1/1 (frame 229/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 2 Protective Bootss, 4 Protective Helmets, 8.7ms
video 1/1 (frame 230/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 4 Protective Bootss, 3 Protective Helmets, 9.0ms
video 1/1 (frame 231/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 3 Protective Bootss, 3 Protective Helmets, 8.7ms
video 1/1 (frame 232/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 3 Protective Bootss, 3 Protective Helmets, 8.8ms
video 1/1 (frame 233/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.4ms
video 1/1 (frame 234/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.0ms
video 1/1 (frame 235/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Bootss, 3 Protective Helmets, 8.7ms
video 1/1 (frame 236/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Bootss, 3 Protective Helmets, 8.7ms
video 1/1 (frame 237/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 3 Protective Bootss, 4 Protective Helmets, 8.7ms
video 1/1 (frame 238/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 3 Protective Bootss, 4 Protective Helmets, 8.7ms
video 1/1 (frame 239/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 3 Protective Bootss, 4 Protective Helmets, 9.0ms
video 1/1 (frame 240/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 5 Protective Bootss, 4 Protective Helmets, 8.9ms
video 1/1 (frame 241/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 3 Protective Bootss, 3 Protective Helmets, 9.0ms
video 1/1 (frame 242/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 2 Protective Bootss, 4 Protective Helmets, 8.7ms
video 1/1 (frame 243/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 2 Protective Bootss, 3 Protective Helmets, 8.8ms
video 1/1 (frame 244/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 2 Protective Bootss, 3 Protective Helmets, 8.8ms
video 1/1 (frame 245/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 1 Protective Boots, 2 Protective Helmets, 9.4ms
video 1/1 (frame 246/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 2 Protective Bootss, 2 Protective Helmets, 9.1ms
video 1/1 (frame 247/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 1 Protective Boots, 2 Protective Helmets, 8.9ms
video 1/1 (frame 248/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 4 Protective Bootss, 3 Protective Helmets, 9.2ms
video 1/1 (frame 249/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 1 Protective Boots, 3 Protective Helmets, 8.9ms
video 1/1 (frame 250/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 1 Protective Boots, 3 Protective Helmets, 8.8ms
video 1/1 (frame 251/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 2 Protective Bootss, 3 Protective Helmets, 8.8ms
video 1/1 (frame 252/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 3 Protective Bootss, 3 Protective Helmets, 8.8ms
video 1/1 (frame 253/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Bootss, 3 Protective Helmets, 8.8ms
video 1/1 (frame 254/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Bootss, 3 Protective Helmets, 9.3ms
video 1/1 (frame 255/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 2 Protective Bootss, 3 Protective Helmets, 8.9ms
video 1/1 (frame 256/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 2 Protective Bootss, 3 Protective Helmets, 8.8ms
video 1/1 (frame 257/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 2 Protective Bootss, 3 Protective Helmets, 9.6ms
video 1/1 (frame 258/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 2 Protective Bootss, 2 Protective Helmets, 8.7ms
video 1/1 (frame 259/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 1 Protective Boots, 2 Protective Helmets, 8.7ms
video 1/1 (frame 260/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 2 Protective Bootss, 3 Protective Helmets, 8.8ms
video 1/1 (frame 261/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 1 Protective Boots, 4 Protective Helmets, 8.6ms
video 1/1 (frame 262/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 1 Protective Boots, 4 Protective Helmets, 9.2ms
video 1/1 (frame 263/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Helmets, 8.6ms
video 1/1 (frame 264/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 4 Protective Helmets, 8.6ms
video 1/1 (frame 265/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 1 Protective Boots, 3 Protective Helmets, 8.7ms
video 1/1 (frame 266/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 1 Protective Boots, 4 Protective Helmets, 9.3ms
video 1/1 (frame 267/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 1 Protective Boots, 4 Protective Helmets, 8.4ms
video 1/1 (frame 268/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 1 Protective Boots, 4 Protective Helmets, 11.3ms
video 1/1 (frame 269/310) /content/PPE_Part1.mp4: 384x640 6 Jackets, 4 Protective Helmets, 8.8ms
video 1/1 (frame 270/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Helmets, 9.2ms
video 1/1 (frame 271/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Helmets, 8.7ms
video 1/1 (frame 272/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Helmets, 9.2ms
video 1/1 (frame 273/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Helmets, 8.9ms
video 1/1 (frame 274/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 3 Protective Helmets, 9.0ms
video 1/1 (frame 275/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Helmets, 8.9ms
video 1/1 (frame 276/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Helmets, 9.4ms
video 1/1 (frame 277/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 2 Protective Helmets, 8.7ms
video 1/1 (frame 278/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 3 Protective Helmets, 9.5ms
video 1/1 (frame 279/310) /content/PPE_Part1.mp4: 384x640 2 Jackets, 3 Protective Helmets, 8.9ms
video 1/1 (frame 280/310) /content/PPE_Part1.mp4: 384x640 2 Jackets, 3 Protective Helmets, 8.9ms
video 1/1 (frame 281/310) /content/PPE_Part1.mp4: 384x640 2 Jackets, 3 Protective Helmets, 8.9ms
video 1/1 (frame 282/310) /content/PPE_Part1.mp4: 384x640 2 Jackets, 3 Protective Helmets, 8.8ms
video 1/1 (frame 283/310) /content/PPE_Part1.mp4: 384x640 5 Jackets, 3 Protective Helmets, 8.6ms
video 1/1 (frame 284/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 3 Protective Helmets, 8.7ms
video 1/1 (frame 285/310) /content/PPE_Part1.mp4: 384x640 2 Jackets, 4 Protective Helmets, 8.8ms
video 1/1 (frame 286/310) /content/PPE_Part1.mp4: 384x640 2 Jackets, 4 Protective Helmets, 8.9ms
video 1/1 (frame 287/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 4 Protective Helmets, 10.2ms
video 1/1 (frame 288/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 2 Protective Helmets, 8.9ms
video 1/1 (frame 289/310) /content/PPE_Part1.mp4: 384x640 2 Jackets, 2 Protective Helmets, 9.0ms
video 1/1 (frame 290/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 1 Protective Helmet, 9.8ms
video 1/1 (frame 291/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 1 Protective Helmet, 8.7ms
video 1/1 (frame 292/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 1 Protective Helmet, 8.7ms
video 1/1 (frame 293/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 1 Protective Helmet, 9.0ms
video 1/1 (frame 294/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 1 Protective Helmet, 9.2ms
video 1/1 (frame 295/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 3 Protective Helmets, 8.8ms
video 1/1 (frame 296/310) /content/PPE_Part1.mp4: 384x640 2 Jackets, 1 Protective Helmet, 8.9ms
video 1/1 (frame 297/310) /content/PPE_Part1.mp4: 384x640 2 Jackets, 2 Protective Helmets, 8.7ms
video 1/1 (frame 298/310) /content/PPE_Part1.mp4: 384x640 2 Jackets, 2 Protective Helmets, 9.0ms
video 1/1 (frame 299/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 2 Protective Helmets, 8.7ms
video 1/1 (frame 300/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 2 Protective Helmets, 8.8ms
video 1/1 (frame 301/310) /content/PPE_Part1.mp4: 384x640 3 Jackets, 2 Protective Helmets, 8.8ms
video 1/1 (frame 302/310) /content/PPE_Part1.mp4: 384x640 2 Jackets, 1 Protective Helmet, 8.7ms
video 1/1 (frame 303/310) /content/PPE_Part1.mp4: 384x640 2 Jackets, 1 Protective Helmet, 8.7ms
video 1/1 (frame 304/310) /content/PPE_Part1.mp4: 384x640 2 Jackets, 1 Protective Helmet, 9.2ms
video 1/1 (frame 305/310) /content/PPE_Part1.mp4: 384x640 2 Jackets, 1 Protective Helmet, 8.7ms
video 1/1 (frame 306/310) /content/PPE_Part1.mp4: 384x640 4 Jackets, 1 Protective Helmet, 8.6ms
video 1/1 (frame 307/310) /content/PPE_Part1.mp4: 384x640 1 Jacket, 1 Protective Helmet, 8.6ms
video 1/1 (frame 308/310) /content/PPE_Part1.mp4: 384x640 1 Jacket, 2 Protective Helmets, 9.1ms
video 1/1 (frame 309/310) /content/PPE_Part1.mp4: 384x640 3 Protective Helmets, 9.2ms
video 1/1 (frame 310/310) /content/PPE_Part1.mp4: 384x640 3 Protective Helmets, 9.0ms
Speed: 2.3ms preprocess, 9.8ms inference, 3.2ms postprocess per image at shape (1, 3, 384, 640)
Results saved to runs/detect/predict3
💡 Learn more at https://docs.ultralytics.com/modes/predict

from IPython.display import HTML
from base64 import b64encode
import os

# Input video path
save_path = '/content/runs/detect/predict3/PPE_Part1.avi'

# Compressed video path
compressed_path = "/content/result_compressed.mp4"

os.system(f"ffmpeg -i {save_path} -vcodec libx264 {compressed_path}")

# Show video
mp4 = open(compressed_path,'rb').read()
data_url = "data:video/mp4;base64," + b64encode(mp4).decode()
HTML("""

""" % data_url)
     


     
