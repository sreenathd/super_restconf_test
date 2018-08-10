*** Settings ***
Library       OperatingSystem
Library       RestConf

*** Variables ***
${MESSAGE}    Hello, world!

*** Test Cases ***
My Test
    [Documentation]    Example test
    Log    ${MESSAGE}
    My Keyword    /tmp

Another Test
    Should Be Equal    ${MESSAGE}    Hello, world!
    
Get Test
    ${result}=  get    /config/hostname 
    Should Be Equal  ${result.status_code}  ${200}
    
*** Keywords ***
My Keyword
    [Arguments]    ${path}
    Directory Should Exist    ${path}
