# Pull in additional identifiers
df = search.steal_bundles_to_dataframe(
    resource_type="Patient",
    request_params={"_has:Procedure:subject:code": "http://snomed.info/sct|16830007"},
    fhir_paths=[
        ("given_name", "Patient.name.where(use = 'official').given"),
        ("family_name", "Patient.name.where(use = 'official').family"),
        ("birth_date", "Patient.birthDate"),
        ("fhir_id", "Patient.id"),
        ("mrn", "Patient.identifier.where(type.coding.system = 'http://terminology.hl7.org/CodeSystem/v2-0203' and type.coding.code = 'MR').value"),
        ("passport", "Patient.identifier.where(type.coding.system = 'http://terminology.hl7.org/CodeSystem/v2-0203' and type.coding.code = 'PPN').value"),
        ("ssn", "Patient.identifier.where(system = 'http://hl7.org/fhir/sid/us-ssn').value")

    ],
    num_pages=1,
)
print(df.T)

search2 = Pirate(
    auth=None, # the demo fhir server does not require authentication
    base_url='https://r4.smarthealthit.org',
)

df2 = search2.steal_bundles_to_dataframe(
    resource_type="Patient",
    request_params={"identifier": f"http://hl7.org/fhir/sid/us-ssn|{df.loc[0, 'ssn']}"},
    fhir_paths=[
        ("given_name", "Patient.name.where(use = 'official').given"),
        ("family_name", "Patient.name.where(use = 'official').family"),
        ("birth_date", "Patient.birthDate"),
        ("fhir_id", "Patient.id"),
        ("ehr_id", "Patient.identifier.where(type.coding.system = 'http://terminology.hl7.org/CodeSystem/v2-0203' and type.coding.code = 'MR').value")
    ],
    num_pages=1,
)

df2