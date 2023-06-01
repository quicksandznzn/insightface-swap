import os
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INSIGHTFACE_SWAPPER_MODEL_PATH = os.path.join(base_path, "models/inswapper_128.onnx")

INSIGHTFACE_FACE_ANALYSIS_NAME = "buffalo_l"

ONNX_PROVIDERS = ["CUDAExecutionProvider", "CPUExecutionProvider"]


print(INSIGHTFACE_SWAPPER_MODEL_PATH)