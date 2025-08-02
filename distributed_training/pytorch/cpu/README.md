# PyTorch Job CPU example


## submit using runai CLI

run this command:
```bash
#!/bin/bash

# RunAI PyTorch Hello World Example
# Equivalent to the PyTorchJob YAML manifest

runai training pytorch submit pytorch-hello-world-cpu \
  -p default \
  -i pytorch/pytorch:1.13.1-cuda11.6-cudnn8-runtime \
  --workers 2 \
  --cpu-core-request 0.1 \
  --cpu-core-limit 0.5 \
  --cpu-memory-request 128Mi \
  --cpu-memory-limit 512Mi \
  --master-cpu-core-request 0.1 \
  --master-cpu-core-limit 0.5 \
  --master-cpu-memory-request 128Mi \
  --master-cpu-memory-limit 512Mi \
  --restart-policy OnFailure \
  --master-restart-policy OnFailure \
  --command \
  -- /bin/bash -c "curl -o /tmp/pytorch-hello-world.py https://myserver.com/scripts/pytorch-hello-world.py && python3 /tmp/pytorch-hello-world.py"
```