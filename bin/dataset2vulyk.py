# -*- encoding: utf-8 -*-
import json
import uuid


def main(input_path):
    unique_filename = str(uuid.uuid4())[:5] + '.json'

    with open(unique_filename, 'w') as fio:
        raw_docs = json.loads(open(input_path).read())
        i = 0
        for x in iter(raw_docs['links']):
            print(i)
            fio.write(json.dumps(x) + '\n')

            if i > 5:
                break
            i += 1


if __name__ == "__main__":
    # input_path = sys.argv[1]
    input_path = '/home/warmonger/Downloads/items/items.json'
    main(input_path)
    # with open('demo')
    # for i in raw_docs['links']:
