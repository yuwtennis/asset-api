STABLE_VERSION ?= $(shell curl -s -XGET https://chromedriver.storage.googleapis.com/LATEST_RELEASE)

download:
	curl -s -O https://chromedriver.storage.googleapis.com/$(STABLE_VERSION)/chromedriver_linux64.zip
	unzip chromedriver_linux64.zip chromedriver -d ./ &&  rm -rf chromedriver_linux64.zip
clean-binary:
	rm -rf chromedriver
