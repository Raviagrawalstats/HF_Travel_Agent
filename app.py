import gradio as gr
from travel_agent.agent import main  # Adjust import as needed

def run_agent(city, days, pref, start_date):
    # You may need to refactor your agent to work as a function, not CLI
    # For now, just a placeholder
    return "Your itinerary here"

iface = gr.Interface(
    fn=run_agent,
    inputs=[
        gr.Textbox(label="City"),
        gr.Number(label="Days"),
        gr.Dropdown(["beach", "mountain", "city", "historical"], label="Preference"),
        gr.Textbox(label="Start Date (YYYY-MM-DD)")
    ],
    outputs="text",
    title="Travel Itinerary Agent"
)

if __name__ == "__main__":
    iface.launch()