torch.save(
    model.state_dict(),
    "model.pth",
)

loaded_model = SimpleCNN()

loaded_model.load_state_dict(
    torch.load("model.pth")
)

loaded_model.eval()

print("Model ready for inference.")