"""Defines the AWS resources for the PDF processing pipeline."""

from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_s3 as s3,
)
from constructs import Construct
from pathlib import Path


class PdfProcessorStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, "UploadBucket")

        handlers_dir = str(Path(__file__).resolve().parents[3] / "handlers")

        upload_fn = _lambda.Function(
            self,
            "UploadHandler",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="pdf_upload_handler.handler",
            code=_lambda.Code.from_asset(handlers_dir),
            environment={"BUCKET": bucket.bucket_name},
        )

        bucket.grant_read_write(upload_fn)

        # Additional Lambda functions would be defined similarly for parsing,
        # previewing, and exporting.
