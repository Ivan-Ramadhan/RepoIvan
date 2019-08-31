from github import Github

def create(repo1):

    token='07ed9eed3e43b90e8e18c53790856746ca38c315'
    g=Github(token)
    user=g.get_user()
    print(user)
    repo=user.create_repo(repo1)


def main():
    repo="RepoIvan"
    create(repo)

if __name__ == "__main__":
    main()
