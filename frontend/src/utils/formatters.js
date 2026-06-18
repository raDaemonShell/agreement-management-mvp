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
