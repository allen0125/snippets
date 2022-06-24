use pyo3::prelude::*;

pub(crate) fn register(py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(determine_current_os, m)?)?;
    Ok(())
}

#[pyfunction]
fn determine_current_os() -> String {
    "linux".to_owned()
}