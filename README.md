# Tank Detection

Real-time tank detection using **YOLOv26s** (Ultralytics). The model is trained on a multi-view tank dataset and supports live inference via webcam.

## Project Structure

```
tank-detection/
├── train.py          # Training script
├── test.py           # Real-time webcam inference
├── weights/
│   └── best.pt       # Trained model weights
├── results/          # Training metrics & visualizations
│   ├── args.yaml
│   ├── results.csv
│   ├── results.png
│   ├── confusion_matrix.png
│   ├── confusion_matrix_normalized.png
│   ├── labels.jpg
│   ├── BoxF1_curve.png
│   ├── BoxPR_curve.png
│   ├── BoxP_curve.png
│   └── BoxR_curve.png
└── README.md
```



## Requirements

- Python 3.8+
- [Ultralytics](https://github.com/ultralytics/ultralytics)
- OpenCV

```bash
pip install ultralytics opencv-python
```

## Training

Edit `train.py` to point to your dataset, then run:

```bash
python train.py
```

**Training configuration highlights:**

| Parameter  | Value    |
| ---------- | -------- |
| Model      | YOLOv26s |
| Image size | 512      |
| Batch size | 48       |
| Epochs     | 100      |

See [`results/args.yaml`](results/args.yaml) for the full list of training arguments.

## Inference (Webcam)

Run real-time detection with a webcam:

```bash
python test.py
```

> Press **Q** to quit the webcam window.

The script loads the trained weights and runs inference at a confidence threshold of **0.80**.

## Results

Training metrics and visualizations are saved in the `results/` directory, including precision-recall curves, F1 curves, and confusion matrices.

## License

This project does not currently specify a license. Add a `LICENSE` file to define usage terms.
