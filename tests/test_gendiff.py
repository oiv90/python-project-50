import os

from gendiff import generate_difference


def test_generate_difference_with_json_files():
    test_data_dir = os.path.join("tests", "test_data")
    file1_path = os.path.join(test_data_dir, "file1.json")
    file2_path = os.path.join(test_data_dir, "file2.json")
    expected_result_path = os.path.join(test_data_dir, "result.txt")

    with open(expected_result_path, "r", encoding="utf-8") as f:
        expected_result = f.read().strip()

    actual_result = generate_difference(
        file1_path, file2_path, format="stylish"
    )

    assert actual_result == expected_result, (
        f"Сгенерированный результат не соответствует ожидаемому.\n"
        f"Ожидали:\n{expected_result}\n\n"
        f"Получили:\n{actual_result}"
    )


def test_generate_difference_files_exist():
    test_data_dir = os.path.join("tests", "test_data")

    required_files = ["file1.json", "file2.json", "result.txt"]

    for filename in required_files:
        file_path = os.path.join(test_data_dir, filename)
        assert os.path.exists(
            file_path
        ), f"Required test file not found: {file_path}"
