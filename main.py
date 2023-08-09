"""Crawl target urls"""
import setting
import helper
import crawler


if __name__ == "__main__":
    program_args = setting.Options().parse()

    # login
    credential = helper.json_to_obj(program_args.asset_path + "credential.json")
    urls = helper.json_to_obj(program_args.asset_path + "target_urls.json")
    driver = crawler.login(program_args.login_url,
                           credential["email"],
                           credential["password"])

    # crawl url
    for url in urls:
        crawler.crawl_url(driver,
                          post_limit=5,
                          target_url=url,
                          screenshot_path=program_args.screenshot_path,
                          )
