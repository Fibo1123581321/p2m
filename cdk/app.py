#!/usr/bin/env python3
"""CDK application entry point."""

from aws_cdk import App
from src.stacks.pdf_processor_stack import PdfProcessorStack

app = App()
PdfProcessorStack(app, "PdfProcessorStack")
app.synth()
