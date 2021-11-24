import torch
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

conversation = html.Div(
    style={
        "width": "80%",
        "max-width": "800px",
        "height": "70vh",
        "margin": "auto",
        "overflow-y": "auto",
    },
    id="display-conversation",
)

controls = dbc.InputGroup(
    style={"width": "80%", "max-width": "800px", "margin": "auto"},
    children=[
        dbc.Input(id="user-input", placeholder="Write to the chatbot...", type="text"),
        dbc.InputGroupAddon(dbc.Button("Submit", id="submit"), addon_type="append",),
    ],
)

layout = dbc.Container(
    fluid=True,
    children=[
        html.H1("Dash Chatbot (with DialoGPT)"),
        html.Hr(),
        dcc.Store(id="store-conversation", data=""),
        conversation,
        controls,
    ],
)

from transformers import AutoModelWithLMHead, AutoTokenizer


device = "cuda" if torch.cuda.is_available() else "cpu"
# device = "cpu"
print(f"Device: {device}")

print("Start loading model...")
name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(name)
model = AutoModelWithLMHead.from_pretrained(name)

# Switch to cuda, eval mode, and FP16 for faster inference
if device == "cuda":
    model = model.half()
model.to(device)
model.eval()

print("Done.")

