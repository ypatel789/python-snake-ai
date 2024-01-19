import torch
if torch.cuda.is_available():
    GPU = torch.cuda.get_device_name(0)
    print(GPU)
else:
    print("GPU Not Available")