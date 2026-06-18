import { reactive } from 'vue'

export const agreementData = reactive({
  counterparty_company: '',

  initiator_name: '',

  initiator_title: '',

  counterparty_contact_name: '',

  counterparty_contact_title: '',

  counterparty_email: '',

  counterparty_phone: '',

  agreement_type: '',

  custom_document: null,

  purpose: '',

  ip_protection: '',

  governing_law: '',

  start_date: '',

  end_date: '',

  duration: '',

  initiator_signature: '',

  expiry_days: 14,
})
