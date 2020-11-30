const fs = require("fs");
const res = JSON.parse(fs.readFileSync("results.json", "utf8"));

arr = res.map((item) => {
	return { ...item };
});

const casesFinal = res.reduce((acc, item, index) => {
	if (index != 0 && index != arr.length - 1) {
		item["Confirmed"] = item["Confirmed"] - arr[index - 1]["Confirmed"];
		item["Deaths"] = item["Deaths"] - arr[index - 1]["Deaths"];
		item["Recovered"] = item["Recovered"] - arr[index - 1]["Recovered"];
		acc.push(item);
	}
	return acc;
}, []);

const json = JSON.stringify(casesFinal);

fs.writeFile("results.json", json, "utf8", () => console.log("DONE!"));
