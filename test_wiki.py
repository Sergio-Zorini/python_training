{
  "id": "15415e9f-f34e-43fb-8144-36bb2d3a548a",
  "version": "1.1",
  "name": "test_wiki.py",
  "url": "https://www.wikipedia.org",
  "tests": [{
    "id": "30b0c34f-6793-4448-9398-1b4d60b38187",
    "name": "test_wiki",
    "commands": [{
      "id": "538fe83f-aab0-48a2-bda8-b71559742f74",
      "comment": "",
      "command": "open",
      "target": "/",
      "targets": [],
      "value": ""
    }, {
      "id": "56565545-c720-49ac-b1d7-084801e2eb6a",
      "comment": "",
      "command": "setWindowSize",
      "target": "550x695",
      "targets": [],
      "value": ""
    }, {
      "id": "5c9f2ed0-7745-4aae-b1d9-ff65a0b34201",
      "comment": "",
      "command": "click",
      "target": "css=#js-link-box-ru > strong",
      "targets": [
        ["css=#js-link-box-ru > strong", "css"],
        ["css=#js-link-box-ru > strong", "css:finder"],
        ["xpath=//a[@id='js-link-box-ru']/strong", "xpath:idRelative"],
        ["xpath=//div[5]/a/strong", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "588e7819-5c95-4afb-bd10-cef83b833d79",
      "comment": "",
      "command": "click",
      "target": "linkText=Избранные статьи",
      "targets": [
        ["linkText=Избранные статьи", "linkText"],
        ["css=a[title=\"Статьи, считающиеся лучшими статьями проекта\"]", "css"],
        ["css=#n-featured > a", "css:finder"],
        ["xpath=//a[contains(text(),'Избранные статьи')]", "xpath:link"],
        ["xpath=//li[@id='n-featured']/a", "xpath:idRelative"],
        ["xpath=(//a[contains(@href, '/wiki/%D0%92%D0%B8%D0%BA%D0%B8%D0%BF%D0%B5%D0%B4%D0%B8%D1%8F:%D0%98%D0%B7%D0%B1%D1%80%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5_%D1%81%D1%82%D0%B0%D1%82%D1%8C%D0%B8')])[2]", "xpath:href"],
        ["xpath=//div[4]/div[2]/div[2]/div/ul/li[4]/a", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "c32484f0-aedb-4d8d-9bdb-d6a662e81f95",
      "comment": "",
      "command": "click",
      "target": "linkText=Добротные статьи",
      "targets": [
        ["linkText=Добротные статьи", "linkText"],
        ["css=a[title=\"Википедия:Добротные статьи\"]", "css"],
        ["css=p:nth-child(1) > a:nth-child(1)", "css:finder"],
        ["xpath=//a[contains(text(),'Добротные статьи')]", "xpath:link"],
        ["xpath=//div[@id='mw-content-text']/div/div/table/tbody/tr/td/div/p/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, '/wiki/%D0%92%D0%B8%D0%BA%D0%B8%D0%BF%D0%B5%D0%B4%D0%B8%D1%8F:%D0%94%D0%BE%D0%B1%D1%80%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D1%81%D1%82%D0%B0%D1%82%D1%8C%D0%B8')]", "xpath:href"],
        ["xpath=//p/a", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "9c1bb605-1bdf-4723-b6b8-9b48f1299b02",
      "comment": "",
      "command": "runScript",
      "target": "window.scrollTo(0,714)",
      "targets": [],
      "value": ""
    }, {
      "id": "9444e977-dafc-41b5-817c-985072055b81",
      "comment": "",
      "command": "click",
      "target": "linkText=Антисербские погромы в Сараеве",
      "targets": [
        ["linkText=Антисербские погромы в Сараеве", "linkText"],
        ["css=li:nth-child(3) > .mw-redirect:nth-child(2)", "css:finder"],
        ["xpath=//a[contains(text(),'Антисербские погромы в Сараеве')]", "xpath:link"],
        ["xpath=//div[@id='mw-content-text']/div/table/tbody/tr/td/table[3]/tbody/tr/td/ul/li[3]/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, '/wiki/%D0%90%D0%BD%D1%82%D0%B8%D1%81%D0%B5%D1%80%D0%B1%D1%81%D0%BA%D0%B8%D0%B5_%D0%BF%D0%BE%D0%B3%D1%80%D0%BE%D0%BC%D1%8B_%D0%B2_%D0%A1%D0%B0%D1%80%D0%B0%D0%B5%D0%B2%D0%B5')]", "xpath:href"],
        ["xpath=//li[3]/a", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "47d28da2-4384-496b-a765-4c5398f58bdf",
      "comment": "",
      "command": "click",
      "target": "css=span.toctext",
      "targets": [
        ["css=span.toctext", "css"],
        ["css=.tocsection-1 .toctext", "css:finder"],
        ["xpath=//div[@id='toc']/ul/li/a/span[2]", "xpath:idRelative"],
        ["xpath=//a/span[2]", "xpath:position"]
      ],
      "value": ""
    }]
  }],
  "suites": [{
    "id": "bd90293a-d998-495c-b44c-1178c4308acf",
    "name": "Default Suite",
    "persistSession": false,
    "parallel": false,
    "timeout": 300,
    "tests": ["30b0c34f-6793-4448-9398-1b4d60b38187"]
  }],
  "urls": ["https://www.wikipedia.org/"],
  "plugins": []
}