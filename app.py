import json
import gradio as gr
import ollama


MODEL = "pcb-inspector"


DEFECT_CLASSES = [
    "missing_component",
    "misplaced_component",
    "wrong_orientation",
    "damaged_component",
    "solder_bridge",
    "insufficient_solder",
    "excessive_solder",
    "lifted_lead",
    "tombstoning",
    "foreign_object",
    "pcb_damage",
    "other"
]


def inspect_pcb(image, defect_label):

    if image is None:
        return {
            "status": "REVIEW",
            "defect": "unknown",
            "confidence": 0.0,
            "evidence": "No image provided."
        }

    if not defect_label:
        return {
            "status": "REVIEW",
            "defect": "unknown",
            "confidence": 0.0,
            "evidence": "No defect label provided."
        }

    prompt = f"""
Inspect the supplied PCB image.

Proposed defect:
{defect_label}

Determine whether this proposed defect is visibly present.

Remember:
- Trust the image, not the label.
- Do not assume the defect exists.
- Do not invent defects.
- Return only the required JSON.
"""

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt,
                "images": [image]
            }
        ],
        format="json",
        stream=False,
        options={
            "temperature": 0.1,
            "top_p": 0.8
        }
    )

    raw = response["message"]["content"]

    try:
        return json.loads(raw)

    except json.JSONDecodeError:
        return {
            "status": "REVIEW",
            "defect": "unknown",
            "confidence": 0.0,
            "evidence": "Model returned invalid JSON."
        }


with gr.Blocks(
    title="PCB Inspection Verifier"
) as demo:

    gr.Markdown(
        "# PCB Inspection Verifier\n"
        "Upload a PCB image and provide the suspected defect."
    )

    with gr.Row():

        image = gr.Image(
            type="filepath",
            label="PCB Image"
        )

        with gr.Column():

            defect = gr.Dropdown(
                choices=DEFECT_CLASSES,
                label="Suspected Defect",
                value="missing_component"
            )

            inspect_button = gr.Button(
                "Inspect PCB",
                variant="primary"
            )

    result = gr.JSON(
        label="Inspection Result"
    )

    inspect_button.click(
        fn=inspect_pcb,
        inputs=[
            image,
            defect
        ],
        outputs=result
    )


if __name__ == "__main__":
    demo.launch()