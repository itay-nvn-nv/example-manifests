# PyTorch Job GPU example


## submit using runai CLI

run this command:
```bash
#!/bin/bash

# RunAI PyTorch Hello World GPU Example
# Equivalent to the PyTorchJob YAML manifest

runai training pytorch submit pytorch-hello-world-gpu \
  -p default \
  -i pytorch/pytorch:2.1.0-cuda12.1-cudnn8-runtime \
  --workers 2 \
  --gpu-devices-request 1 \
  --master-gpu-devices-request 1 \
  --restart-policy OnFailure \
  --master-restart-policy OnFailure \
  --command \
  -- /bin/bash -c "curl -o /tmp/pytorch-gpu-training.py https://raw.githubusercontent.com/itay-nvn-nv/example-manifests/refs/heads/main/distributed_training/pytorch/gpu/script.py && python3 /tmp/pytorch-gpu-training.py"
```