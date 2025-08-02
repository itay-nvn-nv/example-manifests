import torch
import torch.distributed as dist
import os
import socket
import time

def main():
    print("=== PyTorchJob Hello World ===")
    print(f"Hostname: {socket.gethostname()}")
    print(f"PyTorch version: {torch.__version__}")
    print(f"CUDA available: {torch.cuda.is_available()}")
    print(f"CPU count: {torch.get_num_threads()}")
    
    # Force CPU usage
    device = torch.device('cpu')
    print(f"Using device: {device}")
    
    # Check if we're in distributed mode
    if 'RANK' in os.environ:
        rank = int(os.environ['RANK'])
        world_size = int(os.environ['WORLD_SIZE'])
        print(f"Distributed training - Rank: {rank}, World Size: {world_size}")
        
        # Different behavior for master vs worker
        if rank == 0:  # Master
            print("=== Master Node ===")
            # Create a simple tensor operation
            x = torch.tensor([1.0, 2.0, 3.0], device=device)
            y = torch.tensor([4.0, 5.0, 6.0], device=device)
            result = x + y
            print(f"Tensor operation result: {result}")
        else:  # Worker
            print(f"=== Worker Node (Rank {rank}) ===")
            # Simple tensor operation
            x = torch.randn(3, device=device)
            print(f"Worker tensor: {x}")
            
            # Simulate some work
            time.sleep(5)
    else:
        print("Running in single node mode")
        # Single node tensor operation
        x = torch.tensor([1.0, 2.0, 3.0], device=device)
        y = torch.tensor([4.0, 5.0, 6.0], device=device)
        result = x + y
        print(f"Tensor operation result: {result}")
    
    print("=== Hello World Complete ===")

if __name__ == "__main__":
    main()