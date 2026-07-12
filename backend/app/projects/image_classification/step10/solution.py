model.eval()

image = transform(image)

image = image.unsqueeze(0)

with torch.no_grad():

    outputs = model(image)

    _, predicted = torch.max(outputs, 1)

print(
    "Predicted Class:",
    class_names[predicted.item()]
)