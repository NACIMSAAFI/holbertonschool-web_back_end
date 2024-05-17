import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

const handleProfileSignup = async (
  firstName,
  lastName,
  fileName,
) => {
  const list = [];
  try {
    const user = await signUpUser(firstName, lastName);
    list.push({ status: 'fulfilled', value: user });
    await uploadPhoto(fileName);
  } catch (error) {
    list.push({
      status: 'rejected',
      value: error.toString(),
    });
  }
  return list;
};

export default handleProfileSignup;
