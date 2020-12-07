import json
import time

import pytest
from jsonpath import jsonpath
import requests

from service.tag import Tag

class TestTag:
    def setup_class(self):
        self.tag = Tag()
    @pytest.mark.parametrize("tag_id, tag_name",[
        ['et8b3HDQAAoA0lffIubF4vix-7u1ey3Q', 'tag1_new'],
        ['et8b3HDQAAoA0lffIubF4vix-7u1ey3Q', 'tag1_中文'],
        ['et8b3HDQAAoA0lffIubF4vix-7u1ey3Q', 'tag1_[中文]']
        ])
    def test_tag_list(self, tag_id, tag_name):
        group_name = 'python15'
        tag_name = tag_name + time.strftime("%H_%M_%S")
        r = self.tag.list()
        r = self.tag.updata(
            id=tag_id,
            tag_name=tag_name
        )
        r = self.tag.list()
        # tags = [
        #     tag
        #     for group in r.json()['tag_group'] if group['group_name'] == group_name
        #     for tag in group['tag'] if tag['name'] == tag_name
        # ]
        print(jsonpath(r.json(), f"$..[?(@.name=='{tag_name}')]")[0]['name'])
        print(tag_name)
        assert jsonpath(r.json(), f"$..[?(@.name=='{tag_name}')]")[0]['name'] == tag_name
        # assert tags != []



