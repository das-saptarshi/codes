from git import Repo, exc
from typing import List

class CommitHelper:

    languages = {
        'py': 'python',
        'java': 'java'
    }

    portals = {
        'geeksforgeeks': 'GeeksforGeeks',
        'leetcode': 'Leetcode',
        'codevita': 'Codevita',
        'others': 'Other'
    }

    SECTION_SIZE = 3
    PORTAL_INDEX = 0
    PROBLEM_INDEX = 1
    LANGUAGE_INDEX = 2
    EXTENSION_INDEX = 1

    COMMIT_MESSAGE = 'Solve {portal} problem {problem}'
    COMMIT_DESCRIPTION = 'Add {language} solution for {portal} problem {problem}.'

    COMMIT_MESSAGE_KEY = 'commit_message'
    COMMIT_DESCRIPTION_KEY = 'commit_description'
    FILE_KEY = 'file'

    COMMIT_COMMAND = 'git commit -m "{commit_message}" -m "{commit_description}"'

    def __init__(self, repo_path: str = None):
        assert repo_path is not None, 'Repository Path cannot be None.'
        
        self.repo = Repo(path=repo_path)

        try:
            _ = self.repo.git_dir
        except exc.InvalidGitRepositoryError:
            assert True, f'Repository {repo_path} not valid'

        self.repo.git.execute('git restore --staged .')
    
    def is_changes_added(self) -> bool:
        return self.repo.is_dirty(untracked_files=True)

    def get_changes(self) -> List[str]:
        return self.repo.untracked_files

    def commit(self, file: str, commit_message: str, commit_description: str = '') -> None:
        assert file, f'Invalid File: {file}'
        assert commit_message, f'Invalid commit message: {commit_message}'
        assert commit_description, f'Invalid commit description: {commit_description}'

        self.repo.index.add(file)
        self.repo.git.execute(self.COMMIT_COMMAND.format(commit_message=commit_message, commit_description=commit_description))

    def create_commit_details(self, file: str):
        sections = file.split('/')
        assert len(sections) == self.SECTION_SIZE, f'Invalid File Format : {file}'
        assert '.' in sections[self.LANGUAGE_INDEX], f'Invalid File Format : {file}'

        group, extension = sections[self.PORTAL_INDEX], sections[self.LANGUAGE_INDEX].split('.')[self.EXTENSION_INDEX]

        problem = sections[self.PROBLEM_INDEX]
        portal = self.portals.get(group, None)
        language = self.languages.get(extension, None)

        assert portal != None and language != None, f'Invalid Portal: "{portal}" or Language: "{language}" '

        return {
            self.FILE_KEY: file,
            self.COMMIT_MESSAGE_KEY: self.COMMIT_MESSAGE.format(problem=problem, portal=portal),
            self.COMMIT_DESCRIPTION_KEY: self.COMMIT_DESCRIPTION.format(language=language, problem=problem, portal=portal)
        }




import sys
if __name__ == '__main__':
    helper = CommitHelper(repo_path='E:/Repos/codes')
    
    if not helper.is_changes_added():
        print('No Changes...')
        exit(0)
    
    changes = helper.get_changes()
    
    # Create Dictionary of files to Problem Type and Solution Language
    files = [helper.create_commit_details(change) for change in changes]

    # Iterate over the list of changes and print there commit messages
    for file in files:
        print(file)

    # Iterate over the list of changes and commit.
    if len(sys.argv[0]) > 0:
        if 'commit' in sys.argv:
            for file in files:
                helper.commit(**file)