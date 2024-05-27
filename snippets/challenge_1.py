df_procedures = search.steal_bundles_to_dataframe(
    resource_type="Procedure",
    request_params={"subject": PATIENT_FHIR_ID, "_sort": "-date"},
    fhir_paths=[
        ("coding_system", "Procedure.code.coding.system"),
        ("coding_code", "Procedure.code.coding.code"),
        ("coding_display", "Procedure.code.coding.display"),
        ("id", "Procedure.id"),
        ("date", "Procedure.effectiveDateTime"),
        ("value", "Procedure.valueQuantity.value"),
    ],
    num_pages=1,
)

df_procedures
