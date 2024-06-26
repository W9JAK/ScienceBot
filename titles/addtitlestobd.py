from db import create_table, insert_job_titles, delete_all_job_titles

if __name__ == '__main__':
    with open('processed_job_titles.txt', 'r', encoding='utf-8') as f:
        job_titles = [line.strip() for line in f.readlines()]

    create_table()
    delete_all_job_titles()
    insert_job_titles(job_titles)

    print("Job titles have been inserted into the database.")
