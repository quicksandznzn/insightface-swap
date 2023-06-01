import insightface
from insightface.app import FaceAnalysis

from config.config import *

face_analysis = FaceAnalysis(
    name=INSIGHTFACE_FACE_ANALYSIS_NAME, providers=ONNX_PROVIDERS
)
face_analysis.prepare(ctx_id=0, det_size=(640, 640))

face_swapper = insightface.model_zoo.get_model(
    INSIGHTFACE_SWAPPER_MODEL_PATH, download=True, providers=ONNX_PROVIDERS
)


def get_face(img_data):
    """
        get_face
    :param img_data:
    :return:
    """
    analysed = face_analysis.get(img_data)
    try:
        return sorted(analysed, key=lambda x: x.bbox[0])[0]
    except IndexError:
        return None


def swapper(source_img, target_img):
    """
        swapper
    :param source_img:
    :param target_img:
    """
    face = get_face(target_img)
    source_face = get_face(source_img)
    return face_swapper.get(target_img, face, source_face)
