df = search.steal_bundles_to_dataframe(
    resource_type="Patient",
    request_params={"_has:Procedure:subject:code": "http://snomed.info/sct|16830007"},
    fhir_paths=[
        ("given_name", "Patient.name.where(use = 'official').given"),
        ("family_name", "Patient.name.where(use = 'official').family"),
        ("birth_date", "Patient.birthDate"),
        ("fhir_id", "Patient.id"),
        ("ehr_id", "Patient.identifier.where(type.coding.system = 'http://terminology.hl7.org/CodeSystem/v2-0203' and type.coding.code = 'MR').value")
    ],
    num_pages=1,
)

df