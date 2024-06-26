import re


def process_line(line):
    line = re.sub(r'^\d+\.\s+', '', line).strip()
    line = line.replace('\t', ' ')
    line = re.sub(r'(\S+)-\s+(\S+)', r'\1\2', line)
    return line


def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    job_titles = [process_line(line) for line in lines if line.strip()]

    return job_titles


if __name__ == '__main__':
    file_path = 'code/titles/titles.txt'

    job_titles = process_file(file_path)

    with open('processed_job_titles.txt', 'w', encoding='utf-8') as f:
        for title in job_titles:
            f.write(title + '\n')

    print("The file has been filtered and edited")
