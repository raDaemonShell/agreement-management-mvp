const API_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000/api'
export async function createAgreement(data) {
  const response = await fetch(`${API_URL}/agreements/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })

  const json = await response.json()

  if (!response.ok) {
    console.error('API validation errors:', json) // ← shows exact Django errors
    throw new Error(JSON.stringify(json))
  }

  return json
}

export async function updateAgreement(id, data) {
  const response = await fetch(`${API_URL}/agreements/${id}/`, {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  })

  const json = await response.json()

  if (!response.ok) {
    throw new Error(JSON.stringify(json))
  }

  return json
}

export async function signAgreement(id, signature) {
  const response = await fetch(`${API_URL}/agreements/${id}/sign/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      signature,
    }),
  })

  const json = await response.json()

  if (!response.ok) {
    throw new Error(JSON.stringify(json))
  }

  return json
}

export async function sendOtp(id) {
  const response = await fetch(`${API_URL}/agreements/${id}/send_otp/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
  })

  const json = await response.json()

  if (!response.ok) {
    throw new Error(JSON.stringify(json))
  }

  return json
}

export async function getAgreementPdfUrl(id) {
  const response = await fetch(`${API_URL}/agreements/${id}/download_pdf/`)
  const json = await response.json()
  return json.url
}

export async function emailAgreementCopy(id, email) {
  const response = await fetch(`${API_URL}/agreements/${id}/email_copy/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ email }),
  })

  const json = await response.json()

  if (!response.ok) {
    throw new Error(JSON.stringify(json))
  }

  return json
}

export async function verifyOtp(id, code) {
  const response = await fetch(`${API_URL}/agreements/${id}/verify_otp/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ code }),
  })

  const json = await response.json()

  if (!response.ok) {
    throw new Error(JSON.stringify(json))
  }

  return json
}
