.PHONY: validate sample clean

validate:
	python3 scripts/validate_repo.py

sample:
	javac samples/dsa/TwoSumThreeApproaches.java
	java -cp samples/dsa TwoSumThreeApproaches

clean:
	find samples -name '*.class' -delete
