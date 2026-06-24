export function formatStatus(status) {
  if (status === 'DRAFT') {
    return 'Draft'
  }

  if (status === 'SENT') {
    return 'Awaiting Signature'
  }

  if (status === 'SIGNED') {
    return 'Signed'
  }

  return status
}

export function formatDate(dateString) {
  return new Date(dateString).toLocaleDateString()
}

export function formatSignedDate(dateInput) {
  return new Date(dateInput).toLocaleDateString('en-US', {
    month: 'short',
    day: 'numeric',
    year: 'numeric',
  })
}

export function formatSignedTime(dateInput) {
  return new Date(dateInput).toLocaleTimeString('en-US', {
    hour: 'numeric',
    minute: '2-digit',
    timeZoneName: 'short',
  })
}

export function formatInitiatorSignedMeta(title, signedAt) {
  const when = signedAt ? new Date(signedAt) : new Date()
  return `${title} · ${formatSignedDate(when)} · ${formatSignedTime(when)}`
}
