from fileprocess import process_file
from db import create_table, insert_job_titles, delete_all_job_titles

if __name__ == '__main__':
    file_path = 'code/titles/titles.txt'
    processed_file_path = 'code/titles/processed_job_titles.txt'

    job_titles = process_file(file_path)

    with open(processed_file_path, 'w', encoding='utf-8') as f:
        for title in job_titles:
            f.write(title + '\n')

    with open(processed_file_path, 'r', encoding='utf-8') as f:
        job_titles = [line.strip() for line in f.readlines()]

    create_table()
    delete_all_job_titles()
    insert_job_titles(job_titles)

    print("Job titles have been processed and inserted into the database.")
