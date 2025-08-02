import os
import torch
import torch.nn as nn
import torch.optim as optim
import torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel as DDP

# Initialize process group
if 'RANK' in os.environ:
    rank = int(os.environ['RANK'])
    world_size = int(os.environ['WORLD_SIZE'])
    dist.init_process_group(backend='nccl', init_method='env://', world_size=world_size, rank=rank)
    print(f"Initialized process group: rank {rank}/{world_size}")
else:
    print("Running in non-distributed mode")

# Simple neural network
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(10, 5)
        self.fc2 = nn.Linear(5, 1)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Create model and optimizer
model = Net()
if 'RANK' in os.environ:
    # Move model to GPU and wrap with DDP
    model = model.cuda()
    model = DDP(model, device_ids=[rank])
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Generate some dummy data
x = torch.randn(100, 10)
y = torch.randn(100, 1)
if 'RANK' in os.environ:
    x = x.cuda()
    y = y.cuda()

# Training loop
print(f"Starting training on rank {os.environ.get('RANK', '0')}...")
for epoch in range(10):
    optimizer.zero_grad()
    output = model(x)
    loss = nn.MSELoss()(output, y)
    loss.backward()
    optimizer.step()
    print(f"Rank {os.environ.get('RANK', '0')}, Epoch {epoch+1}, Loss: {loss.item():.4f}")

print(f"Training completed on rank {os.environ.get('RANK', '0')}!")
print("Hello from PyTorchJob!")