from ModuleB import moduleB
from scrape_names import has_name
from attack import attack_all_websites

def main():
    # Get list of users we want to test
    with open('targets.txt', 'r') as target_file:
        for target in target_file:
            target = target.strip()
            if has_name(target):
                extractor = moduleB(target)
                extractor.write_file()
                attack_all_websites(extractor)


if __name__ == '__main__':
    main()

