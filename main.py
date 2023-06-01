import gradio as gr

from utils.face_util import swapper


def swap(source_img, target_img):
    """
        swap
    :param source_img:  source_img
    :param target_img:  target_img
    :return:
    """
    swap_img = swapper(source_img, target_img)
    return swap_img


if __name__ == "__main__":
    app = gr.Interface(
        fn=swap, inputs=["image", "image"], outputs=gr.Image()
    )
    app.launch(server_name="0.0.0.0")
