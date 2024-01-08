import csv
from pathlib import Path
import shutil


def read_contacts_from_file(file_name, target_path):
    path = Path(target_path)
    not_found = []  # Створюємо список для відстеження незнайдених ідентифікаторів

    with open(file_name, "r", newline="") as file:
        read = csv.DictReader(file)

        for el in read:
            original_id = el['original_id']
            target_folder = el["seson"]
            create_folder = path.joinpath(target_folder)
            create_folder.mkdir(exist_ok=True)

            found = False  # Прапор для відстеження знайдених файлів

            for video_file in path.iterdir():
                file_name = video_file.stem

                if original_id in file_name:
                    new_file_name = create_folder.joinpath(video_file.name)
                    shutil.move(video_file, new_file_name)
                    print(f"Перенесено {video_file.name}")
                    found = True
                    break

            if not found:
                # Якщо файл не знайдено, додаємо ідентифікатор до списку
                not_found.append(original_id)

    if not_found:
        with open("result.csv", "w", newline="") as file:
            header = ["original_id"]
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()

            for id_ in not_found:
                writer.writerow({"original_id": id_})


file_name = "name.csv"
target_path = "path"


read_contacts_from_file(file_name, target_path)
