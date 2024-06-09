from argparse import ArgumentParser
import logging
import json
from pathlib import Path
from urllib.parse import urljoin

import pandas as pd
import requests


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s\t%(module)s\t[%(levelname)s]\t%(message)s",
)
log = logging.getLogger()


def make_new_post(address: str, post: dict):
    required_fields = "author", "body", "tags", "title"
    log.debug("Validate at least one of the required field is present")
    assert any([key in required_fields for key in post.keys()]), f"The post must have at least one of the followinf fields: {required_fields}"
    
    endpoint = urljoin(address, "posts")
    log.info(f"Post {post} to {endpoint}")
    res = requests.post(endpoint, data=json.dumps(post), headers={
        "content-type": "application/json"
      })
    log.info(f"Response code: {res.status_code}")
    assert res.status_code == 200, "Failed to write data"


def fetch_data(address: str):
    endpoint = urljoin(address, "posts")
    log.info(f"Get data from {endpoint}")
    res = requests.get(endpoint)
    log.info(f"Response code: {res.status_code}")
    assert res.status_code == 200, "Failed to fetch data"
    return res.json()


def dump_to_csv(address: str, out_file: Path):
    data = fetch_data(address)
    log.info(f"Dump database to {out_file} as csv")
    df = pd.DataFrame(data)
    df.to_csv(out_file)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("address", 
                        help="IP address with protocol (http/s://)"
                        )
    args = parser.parse_args()
    sample_data = {
        "author": "giulio",
        "title": "assignment"
    }
    address = args.address
    make_new_post(address, sample_data)
    dump_to_csv(address, "db_dump.csv")
