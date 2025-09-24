# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Data models for AWS Documentation MCP Server."""

from pydantic import BaseModel, Field
from typing import Optional, List


class SearchResult(BaseModel):
    """Search result from AWS documentation search."""

    rank_order: int
    url: str
    title: str
    context: Optional[str] = None


class RecommendationResult(BaseModel):
    """Recommendation result from AWS documentation."""

    url: str
    title: str
    context: Optional[str] = None


class AWSPreferences(BaseModel):
    """AWS preferences for customizing documentation recommendations."""

    region: Optional[str] = Field(
        default=None,
        description='AWS region (e.g., "us-east-1", "eu-west-1")'
    )
    services: Optional[List[str]] = Field(
        default=None,
        description='List of AWS services (e.g., ["s3", "lambda", "ec2"])'
    )
    use_case: Optional[str] = Field(
        default=None,
        description='Detailed primary use case describing architecture, services, and purpose (e.g., "serverless web applications with API Gateway, Lambda functions, and DynamoDB for user authentication and data storage", "data analytics pipeline using S3, Glue, and Redshift for ETL processing", "machine learning workflows with SageMaker, S3, and Lambda for model training and inference")'
    )
    documentation_depth: Optional[str] = Field(
        default=None,
        description='Preferred documentation depth: "overview" for high-level concepts, "detailed" for comprehensive guides, or "reference" for API specifications and technical details'
    )
