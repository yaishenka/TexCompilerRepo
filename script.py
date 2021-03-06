import os

def compile_files():
	sources_dir = 'src/'
	compiled_dir = 'compiled/'

	file_list = os.listdir(sources_dir)

	for file in file_list:
		if 'DS_Store' in file: # Костыль
			continue
		print(file)
		os.system('pdflatex -output-directory={0} {1}'.format(compiled_dir, os.path.join(sources_dir, file)))	

if 'Travis build' not in os.environ['TRAVIS_COMMIT_MESSAGE']:
	compile_files()


