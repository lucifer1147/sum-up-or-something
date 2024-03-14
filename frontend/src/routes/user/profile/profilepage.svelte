<script>
	import { browser } from '$app/environment';
	import tokens from '$lib/shared/store/jwt.js';

	export let data;

	let formData = browser
		? {
				...data.json
			}
		: {
				first_name: '',
				last_name: '',
				email: '',
				username: '',
				description: ''
			};

	$: for (const [key, val] of Object.entries(formData)) {
		if (val === 'not-set') {
			formData[key] = '';
		}
	}

	let conv_form_data;

	$: conv_form_data = {
		...formData
	};

	$: for (const [key, val] of Object.entries(conv_form_data)) {
		if (val === '') {
			conv_form_data[key] = 'not-set';
		}
	}

	const handleSubmit = async (e) => {
		let success = false;
		let errors;
		let request_form_data = new FormData();

		for (const [key, val] of Object.entries(conv_form_data)) {
			if (key !== 'profile_photo') {
				request_form_data.append(key, val);
			}
		}

		let request_data = {
			method: 'PATCH',
			headers: {
				Authorization: `Bearer ${tokens.access}`
				// 'Content-Type': 'multipart/form-data'
			},
			body: request_form_data
		};

		let response = await fetch('http://localhost:8000/auth/api/users/me/', request_data);
		if (response.ok) {
			success = true;
		}

		let resp = await response.json();
		if (success !== true) {
			for (const [key, value] of Object.entries(resp)) {
				console.log(key, value);
			}
		}
	};

	const handleReset = () => {
		formData = browser
			? {
					...data.json
				}
			: {
					first_name: '',
					last_name: '',
					email: '',
					username: '',
					description: ''
				};
	};
</script>

<div class="h-full">
	<form
		class="m-10 px-16 py-10 rounded-lg bg-gray-200 grid grid-cols-4 h-[calc(100%-120px)] overflow-auto font-bold font-mono items-center gap-y-5"
		on:submit|preventDefault={handleSubmit}
		on:reset={handleReset}
		method="post"
		enctype="multipart/form-data"
	>
		<div class="h-full w-full flex items-center text-lg rounded-l-3xl bg-gray-400 px-5">
			First Name:
		</div>
		<input
			type="text"
			bind:value={formData.first_name}
			class="col-span-3 px-5 rounded-r-3xl font-normal h-full"
			placeholder="Set your First Name here..."
		/>
		<div class="h-full w-full flex items-center text-lg rounded-l-3xl bg-gray-400 px-5">
			Last Name:
		</div>
		<input
			type="text"
			bind:value={formData.last_name}
			class="col-span-3 px-5 rounded-r-3xl font-normal h-full"
			placeholder="Set your Last Name here..."
		/>

		<div class="h-full w-full flex items-center text-lg rounded-l-3xl bg-gray-400 px-5">
			UserName:
		</div>
		<input
			type="text"
			bind:value={formData.username}
			class="col-span-3 px-5 rounded-r-3xl font-normal h-full"
			placeholder="Set your Username here..."
		/>

		<div class="h-full w-full flex items-center text-lg rounded-l-3xl bg-gray-400 px-5 row-span-3">
			Description:
		</div>
		<textarea
			type="text"
			bind:value={formData.description}
			class="col-span-3 py-3 pr-7 px-5 rounded-r-3xl font-normal h-full row-span-3 resize-none"
			placeholder="Set a description for youself here..."
		/>

		<div class="col-span-4 flex h-full gap-x-1">
			<button type="submit" class="bg-slate-800 text-white text-xl rounded-l-3xl w-1/2"
				>Save Changes</button
			>
			<button on:click={handleReset} class="bg-slate-800 text-white text-xl rounded-r-3xl w-1/2"
				>Reset Changes</button
			>
		</div>
	</form>
</div>
