*** Settings ***
Library       OperatingSystem
Library       RestConf
Library    Collections

*** Variables ***
${MESSAGE}    Hello, world!

*** Test Cases ***
Verify Hostname
    ${result}=  get    system:system/config 
    Should Be Equal  ${result.status_code}  ${200}
    ${json}=  Set Variable  ${result.json()}
    Log    ${json}
    json property should equal    ${json}    system:system    config 
    
Verify Post
    ${result}=  post    system:system/config    {"system:system": "config"}
    Should Be Equal  ${result.status_code}  ${200}
    ${json}=  Set Variable  ${result.json()}
    Log    ${json}
    json property should equal    ${json}    system:system    config  
    
*** Keywords ***
json_property_should_equal    
    [Arguments]  ${json}  ${property}  ${value_expected}
    ${value_found} =    Get From Dictionary  ${json}  ${property}
    ${error_message} =  Catenate  SEPARATOR=  Expected value for property "  ${property}  " was "  ${value_expected}  " but found "  ${value_found}  "
    Should Be Equal As Strings  ${value_found}  ${value_expected}  ${error_message}    values=false

