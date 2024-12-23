use solana_program::{
    account_info::{next_account_info, AccountInfo},
    entrypoint,
    entrypoint::ProgramResult,
    program_error::ProgramError,
    pubkey::Pubkey,
};

entrypoint!(process_instruction);

pub fn process_instruction(
    _program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let account = next_account_info(accounts_iter)?;

    if account.is_signer {
        msg!("Account is signed. Proceeding with genetic data validation.");
        // Example Validation Logic
        if instruction_data.len() > 0 {
            msg!("Received genetic data successfully!");
        } else {
            msg!("No data received. Exiting.");
            return Err(ProgramError::InvalidInstructionData);
        }
    }

    Ok(())
}
