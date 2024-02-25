def numUniqueEmails(self, emails):
      unique_emails = set()
      for email in emails:
          local_name, domain_name = email.split('@')
          local_name = local_name.split('+')[0].replace('.', '')
          modified_email = local_name + '@' + domain_name
          unique_emails.add(modified_email)

      return len(unique_emails)
