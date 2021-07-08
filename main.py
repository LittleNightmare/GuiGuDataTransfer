import json


def get_data_from_villain(villain_path) -> (list, list):
    # LocalText物品对应的名字
    with open(villain_path + "/base/LocalText.json", encoding='UTF-8') as t:
        local_text = json.loads(t.read())
    # ItemProps有所有的物品
    with open(villain_path + "/base/ItemProps.json", encoding='UTF-8') as item:
        item_props = json.loads(item.read())
    return local_text, item_props


def generate_csv(obj: dict):
    with open("ItemIDs.csv", mode="w+", encoding='UTF-8') as c:
        for key, value in obj.items():
            c.write(str(key) + "," + value + "\n")


def generate_item_list(path):
    local_text, item_props = get_data_from_villain(path)
    items: dict = {}

    for item in item_props:
        for text in local_text:
            if text.get("key") == item.get("name"):
                if text.get("ch") == "功法" or text.get("ch") == "衣服":
                    continue
                # ch为中文
                items[item.get("id")] = text.get("ch")

    generate_csv(items)
    print("Generated " + path)


if __name__ == '__main__':
    path = "D:/Steam/steamapps/common/鬼谷八荒/Mods/Villain"
    generate_item_list(path)
