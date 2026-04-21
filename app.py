import gradio as gr

# 一个最简单的示例函数：输入文字 → 输出反转文字
def reverse_text(text):
    return text[::-1]

# Gradio 界面
with gr.Blocks(title="我的Gradio应用") as demo:
    gr.Markdown("# 🚀 部署成功！这是你的 Gradio 页面")
    input_text = gr.Textbox(label="输入文字")
    output_text = gr.Textbox(label="反转结果")
    btn = gr.Button("点击反转")
    btn.click(reverse_text, inputs=input_text, outputs=output_text)

# 关键：必须监听 0.0.0.0 和 7860 端口（容器内部固定）
if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860
    )
