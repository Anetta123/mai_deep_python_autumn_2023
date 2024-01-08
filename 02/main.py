import json
import time


def parse_json(
    json_str: str, keyword_callback=None, required_fields=None, keywords=None
):
    try:
        json_doc = json.loads(json_str)
    except json.JSONDecodeError:
        print("Error! You need to set first argument as JSON string type!")
        exit(0)
    except TypeError:
        print("Error! Please, provide string type first argument")
        exit(0)

    if (
        callable(keyword_callback)
        and required_fields is not None
        and keywords is not None
    ):
        for key, value in json_doc.items():
            if key in required_fields:
                value = value.split(" ")
                for item in value:
                    if item in keywords:
                        keyword_callback(item)
    else:
        print(
            "Make sure that you provided 'keyword_callback',"
            " 'required_fields',"
            " 'keywords' arguments"
        )


def mean(k):
    def timer(fn):
        def wrapper(value):
            start = time.time()
            res = fn(value)
            end = time.time()

            length = end - start
            print(f"YOUR LENGTH IS: {length:.10f}")
            wrapper.time_.append(length)
            print(len(wrapper.time_))
            if len(wrapper.time_) < k:
                print(f"{(sum(wrapper.time_) / len(wrapper.time_)):.10f}")
            else:
                print(
                    sum(wrapper.time_[len(wrapper.time_) - k : len(wrapper.time_)])
                    / len(wrapper.time_)
                )
            return res

        wrapper.time_ = []
        return wrapper

    return timer


@mean(5)
def print_upper(value: str):
    print(value.upper())


# print_upper = timer(print_upper)
# print_upper = wrapper()


def main():
    json_string = '{"key1": "Word1 word2", "key2": "word2 word3"}'
    parse_json(json_string, print_upper, ["key2"], ["word3", "word2"])


if __name__ == '__main__':
    main()
